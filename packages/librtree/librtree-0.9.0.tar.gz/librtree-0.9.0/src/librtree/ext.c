/*
  This is the librtree.ext module, defining the PyRTree and
  PyRTreeStyle classes which wrap arounf the functionality of
  librtree.  They are exported as librtree.ext.RTree etc and
  instances are stored as the _rtree members of the Python
  RTree class.
*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

#include "rtree.h"
#include "rtree/package.h"

#include <limits.h>

/*
  given an (open) IO object, create a FILE* to the same filen, we
  extract the fileno from the IO object, dup(2) it and attach a
  buffered stream to it, so the result needs to be fclose()ed in
  the usual manner.
*/

static FILE* io_stream(PyObject *io_obj, const char *mode)
{
  PyObject *fd_obj = PyObject_CallMethod(io_obj, "fileno", NULL);

  if (fd_obj == NULL)
    {
      PyErr_Format(PyExc_ValueError, "io has no fileno attribute");
      return NULL;
    }

  long fd_long = PyLong_AsLong(fd_obj);

  Py_DECREF(fd_obj);

  if ((fd_long < INT_MIN) || (fd_long > INT_MAX))
    {
      PyErr_Format(PyExc_ValueError, "fileno not integer (%li)", fd_long);
      return NULL;
    }

  int fd = fd_long, fd_dup = dup(fd);
  FILE *st;

  if ((st = fdopen(fd_dup, mode)) == NULL)
    {
      PyErr_SetFromErrno(PyExc_RuntimeError);
      return NULL;
    }

  return st;
}

/* PyRTreeStyle Object */

typedef struct
{
  PyObject_HEAD
  style_t *style;
} PyRTreeStyleObject;

static PyTypeObject PyRTreeStyleType;

static int
PyRTreeStyle_Check(PyObject *obj)
{
  if (PyObject_IsInstance(obj, (PyObject*)&PyRTreeStyleType))
    return 1;
  else
    return 0;
}

static PyObject*
PyRTreeStyle_new(PyTypeObject *type, PyObject *args, PyObject *kwarg)
{
  PyRTreeStyleObject *self;

  if ((self = (PyRTreeStyleObject*)type->tp_alloc(type, 0)) != NULL)
    {
      self->style = NULL;
      return (PyObject*)self;
    }

  return NULL;
}

static int
PyRTreeStyle_init(PyRTreeStyleObject *self, PyObject *args, PyObject *kwds)
{
  return 0;
}

static void
PyRTreeStyle_dealloc(PyRTreeStyleObject *self)
{
  postscript_style_destroy(self->style);
  Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject*
PyRTreeStyle_json_read(PyTypeObject *type, PyObject *io_obj)
{
  FILE *st;

  if ((st = io_stream(io_obj, "r")) == NULL)
    return NULL;

  style_t *style = postscript_style_read(st);

  fclose(st);

  if (style == NULL)
    return PyErr_Format(PyExc_RuntimeError, "reading style");

  PyRTreeStyleObject *instance =
    (PyRTreeStyleObject*)PyRTreeStyle_new(type, NULL, NULL);

  if (instance != NULL)
    {
      instance->style = style;
      return (PyObject*)instance;
    }

  postscript_style_destroy(style);

  return NULL;
}

#define PRS_METH(base, args) \
  { #base, (PyCFunction)(PyRTreeStyle_ ## base), args, NULL }

static PyMethodDef PyRTreeStyle_methods[] =
  {
    PRS_METH(json_read, METH_O | METH_CLASS),
    { NULL }
  };

static PyTypeObject PyRTreeStyleType =
  {
   PyVarObject_HEAD_INIT(NULL, 0)
   .tp_name = "librtree.ext.RTreeStyle",
   .tp_doc = PyDoc_STR("RTreeStyle object"),
   .tp_basicsize = sizeof(PyRTreeStyleObject),
   .tp_itemsize = 0,
   .tp_flags = Py_TPFLAGS_DEFAULT,
   .tp_new = PyRTreeStyle_new,
   .tp_init = (initproc)PyRTreeStyle_init,
   .tp_dealloc = (destructor)PyRTreeStyle_dealloc,
   .tp_methods = PyRTreeStyle_methods
  };

/* PyRTree Object */

typedef struct
{
  PyObject_HEAD
  rtree_t *rtree;
} PyRTreeObject;

static PyTypeObject PyRTreeType;

static int PyRTree_Check(PyObject *obj)
{
  if (PyObject_IsInstance(obj, (PyObject*)&PyRTreeType))
    return 1;
  else
    return 0;
}

/*
  constructor: the new/init split in the Python contruction applies
  here only the to Python object, the wrapped rtree_t structure is
  allocated and initialised only in the Python init(), this is so that
  we can naturally use the Python new() in the class methods which
  load an rtree_t from file and so on.
*/

static PyObject* PyRTree_new(PyTypeObject *type, PyObject *args, PyObject *kwarg)
{
  PyRTreeObject *self;

  if ((self = (PyRTreeObject*)type->tp_alloc(type, 0)) != NULL)
    {
      self->rtree = NULL;
      return (PyObject*)self;
    }

  return NULL;
}

static int PyRTree_init(PyRTreeObject *self, PyObject *args, PyObject *kwds)
{
  unsigned long dim;
  unsigned int flags;

  if (PyArg_ParseTuple(args, "ki", &dim, &flags) == 0)
    return -1;

  rtree_t *rtree;

  if ((rtree = rtree_alloc()) == NULL)
    PyErr_SetFromErrno(PyExc_MemoryError);
  else
    {
      int err;

      if ((err = rtree_init(rtree, dim, flags)) == RTREE_OK)
        {
          self->rtree = rtree;
          return 0;
        }

      PyErr_Format(PyExc_ValueError, "rtree_init: %s", rtree_strerror(err));
      rtree_destroy(rtree);
    }

  return -1;
}

static void PyRTree_dealloc(PyRTreeObject *self)
{
  rtree_destroy(self->rtree);
  Py_TYPE(self)->tp_free((PyObject*)self);
}

/* class methods */

static PyObject*
PyRTree_csv_read(PyTypeObject *type, PyObject *args)
{
  PyObject
    *io_obj,
    *dim_obj,
    *flags_obj;

  if (! PyArg_UnpackTuple(args, "csv-read", 3, 3, &io_obj, &dim_obj, &flags_obj))
    return NULL;

  if (! PyLong_Check(dim_obj))
    return PyErr_Format(PyExc_TypeError, "dim not an int");

  long dim_long = PyLong_AsLong(dim_obj);

  if (dim_long < 0)
    return PyErr_Format(PyExc_ValueError, "dim negative");

  size_t dim = dim_long;

  if (! PyLong_Check(flags_obj))
    return PyErr_Format(PyExc_TypeError, "flags not an int");

  long flags_long = PyLong_AsLong(flags_obj);

  if (flags_long < 0)
    return PyErr_Format(PyExc_ValueError, "flags negative");

  state_flags_t flags = flags_long;

  FILE *st;

  if ((st = io_stream(io_obj, "r")) == NULL)
    return NULL;

  rtree_t *rtree = rtree_csv_read(st, dim, flags);

  fclose(st);

  if (rtree == NULL)
    return PyErr_Format(PyExc_RuntimeError, "reading csv");

  PyRTreeObject *instance = (PyRTreeObject*)PyRTree_new(type, NULL, NULL);

  if (instance != NULL)
    {
      instance->rtree = rtree;
      return (PyObject*)instance;
    }

  rtree_destroy(rtree);

  return NULL;
}

static PyObject*
PyRTree_json_read(PyTypeObject *type, PyObject *io_obj)
{
  FILE *st;

  if ((st = io_stream(io_obj, "r")) == NULL)
    return NULL;

  rtree_t *rtree = rtree_json_read(st);

  fclose(st);

  if (rtree == NULL)
    return PyErr_Format(PyExc_RuntimeError, "reading JSON");

  PyRTreeObject *instance = (PyRTreeObject*)PyRTree_new(type, NULL, NULL);

  if (instance != NULL)
    {
      instance->rtree = rtree;
      return (PyObject*)instance;
    }

  rtree_destroy(rtree);

  return NULL;
}

static PyObject*
PyRTree_bsrt_read(PyTypeObject *type, PyObject *io_obj)
{
  FILE *st;

  if ((st = io_stream(io_obj, "rb")) == NULL)
    return NULL;

  rtree_t *rtree = rtree_bsrt_read(st);

  fclose(st);

  if (rtree == NULL)
    return PyErr_Format(PyExc_RuntimeError, "reading JSON");

  PyRTreeObject *instance = (PyRTreeObject*)PyRTree_new(type, NULL, NULL);

  if (instance != NULL)
    {
      instance->rtree = rtree;
      return (PyObject*)instance;
    }

  rtree_destroy(rtree);

  return NULL;
}

/* properies */

static PyObject*
PyRTree_size(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  unsigned long size = rtree_bytes(self->rtree);
  return PyLong_FromUnsignedLong(size);
}

static PyObject*
state_size_access(PyRTreeObject *self, size_t (*f)(const state_t*))
{
  const rtree_t *rtree = self->rtree;
  unsigned long size = f(rtree->state);
  return PyLong_FromUnsignedLong(size);
}

static PyObject*
PyRTree_dim(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  return state_size_access(self, state_dims);
}

static PyObject*
PyRTree_page_size(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  return state_size_access(self, state_page_size);
}

static PyObject*
PyRTree_node_size(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  return state_size_access(self, state_node_size);
}

static PyObject*
PyRTree_rect_size(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  return state_size_access(self, state_rect_size);
}

static PyObject*
PyRTree_branch_size(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  return state_size_access(self, state_branch_size);
}

static PyObject*
PyRTree_branching_factor(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  return state_size_access(self, state_branching_factor);
}

static PyObject*
PyRTree_unit_sphere_volume(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  const rtree_t *rtree = self->rtree;
  double volume = state_unit_sphere_volume(rtree->state);
  return PyFloat_FromDouble(volume);
}

static PyObject*
PyRTree_height(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  rtree_height_t height = rtree_height(self->rtree);
  return PyLong_FromUnsignedLong(height);
}

static PyObject*
PyRTree_empty(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  if (rtree_empty(self->rtree))
    Py_RETURN_TRUE;
  else
    Py_RETURN_FALSE;
}

/* instance methods */

static PyObject*
PyRTree_add_rect(PyRTreeObject *self, PyObject *args)
{
  PyObject *tuple;
  rtree_id_t id;

  if (PyArg_ParseTuple(args, "lO!", &id, &PyTuple_Type, &tuple) == 0)
    return NULL;

  size_t dim = state_dims(self->rtree->state);
  Py_ssize_t len = PyTuple_Size(tuple);

  if (len != 2 * (Py_ssize_t)dim)
    return PyErr_Format(PyExc_ValueError, "bad coordinate tuple size %li", len);

  double coords[2 * dim];

  for (Py_ssize_t i = 0 ; i < len ; i++)
    {
      PyObject *coord;

      if ((coord = PyTuple_GetItem(tuple, i)) == NULL)
        return NULL;

      coords[i] = PyFloat_AsDouble(coord);

      Py_DECREF(coord);
    }

  PyObject *error_type;

  if ((error_type = PyErr_Occurred()) != NULL)
    return PyErr_Format(error_type, "extracting coordinate values");

  int err = rtree_add_rect(self->rtree, id, coords);

  if (err != RTREE_OK)
    return PyErr_Format(PyExc_RuntimeError,
                        "rtree_add_rect: %s",
                        rtree_strerror(err));

  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject*
PyRTree_identical(PyRTreeObject *self, PyObject *other)
{
  if (PyRTree_Check(other))
    {
      if (rtree_identical(self->rtree, ((PyRTreeObject*)other)->rtree))
        Py_RETURN_TRUE;
    }

  Py_RETURN_FALSE;
}

static PyObject*
PyRTree_clone(PyRTreeObject *self, PyObject *Py_UNUSED(ignored))
{
  PyTypeObject *type = Py_TYPE(self);
  PyRTreeObject *clone = (PyRTreeObject*)PyRTree_new(type, NULL, NULL);

  if (clone == NULL)
    return NULL;

  if ((clone->rtree = rtree_clone(self->rtree)) == NULL)
    {
      Py_DECREF(clone);
      return PyErr_SetFromErrno(PyExc_RuntimeError);
    }

  return (PyObject*)clone;
}

typedef struct
{
  PyObject *f, *context;
  size_t dim;
} update_cb_context_t;

static int update_cb(rtree_id_t id, rtree_coord_t *rect, void *varg)
{
  update_cb_context_t *arg = varg;
  size_t dim = arg->dim;

  PyObject
    *cb_arg = NULL,
    *id_obj = PyLong_FromLong(id);

  if (id_obj != NULL)
    {
      PyObject *rect_obj;

      if ((rect_obj = PyTuple_New(2 * dim)) != NULL)
        {
          for (size_t i = 0 ; i < 2 * dim ; i++)
            {
              PyObject *coord_obj;

              if ((coord_obj = PyFloat_FromDouble(rect[i])) != NULL)
                PyTuple_SetItem(rect_obj, i, coord_obj);
            }

          cb_arg = PyTuple_Pack(3, id_obj, rect_obj, arg->context);

          Py_DECREF(rect_obj);
        }

      Py_DECREF(id_obj);
    }

  if (cb_arg == NULL)
    return 1;

  PyObject *rect_obj = PyObject_Call(arg->f, cb_arg, NULL);

  Py_DECREF(cb_arg);

  if (rect_obj == NULL)
    return 1;

  int err = 0;

  if (PyTuple_Check(rect_obj))
    {
      Py_ssize_t len = PyTuple_Size(rect_obj);

      if (len == (Py_ssize_t)(2 * dim))
        {
          for (size_t i = 0 ; i < 2 * dim ; i++)
            {
              PyObject *coord_obj;

              if ((coord_obj = PyTuple_GetItem(rect_obj, i)) != NULL)
                {
                  if (PyFloat_Check(coord_obj))
                    rect[i] = PyFloat_AsDouble(coord_obj);
                  else
                    {
                      PyErr_Format(PyExc_TypeError,
                                   "callback returned tuple contains non-float");
                      err++;
                    }

                  Py_DECREF(coord_obj);
                }
              else
                err++;
            }
        }
      else
        {
          PyErr_Format(PyExc_ValueError, "callback returned %li-tuple", len);
          err++;
        }
    }
  else
    {
      PyErr_Format(PyExc_TypeError, "callback returned non-tuple");
      err++;
    }

  Py_DECREF(rect_obj);

  return err ? 1 : 0;
}

static PyObject*
PyRTree_update(PyRTreeObject *self, PyObject *args)
{
  PyObject *f_obj, *context_obj;

  if (PyArg_UnpackTuple(args, "update", 2, 2, &f_obj, &context_obj))
    {
      if (! PyCallable_Check(f_obj))
        return PyErr_Format(PyExc_TypeError, "function not callable");

      size_t dim = state_dims(self->rtree->state);
      update_cb_context_t context =
        {
          .f = f_obj,
          .context = context_obj,
          .dim = dim
        };

      if (rtree_update(self->rtree, update_cb, &context) != RTREE_OK)
        return NULL;
    }

  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject*
PyRTree_postscript(PyRTreeObject *self, PyObject *args)
{
  PyObject
    *style_obj,
    *axis_obj,
    *extent_obj,
    *margin_obj,
    *io_obj;

  if (PyArg_UnpackTuple(args,
                        "postscript", 5, 5,
                        &style_obj,
                        &axis_obj,
                        &extent_obj,
                        &margin_obj,
                        &io_obj))
    {
      if (! PyRTreeStyle_Check(style_obj))
        return PyErr_Format(PyExc_TypeError, "not a style");

      style_t *style = ((PyRTreeStyleObject*)style_obj)->style;

      if (! PyLong_Check(axis_obj))
        return PyErr_Format(PyExc_TypeError, "not an axis");

      long axis_long = PyLong_AsLong(axis_obj);
      extent_axis_t axis;

      switch (axis_long)
        {
        case axis_width:
        case axis_height:
          axis = axis_long;
          break;
        default:
          return PyErr_Format(PyExc_ValueError, "axis");
        }

      double extent = PyFloat_AsDouble(extent_obj);

      if (extent == -1)
        {
          PyObject *error_type;

          if ((error_type = PyErr_Occurred()) != NULL)
            return PyErr_Format(error_type, "extent");
        }

      double margin = PyFloat_AsDouble(margin_obj);

      if (margin == -1)
        {
          PyObject *error_type;

          if ((error_type = PyErr_Occurred()) != NULL)
            return PyErr_Format(error_type, "margin");
        }

      FILE *st;

      if ((st = io_stream(io_obj, "w")) == NULL)
        return NULL;

      rtree_postscript_t postscript =
        {
          .style = style,
          .axis = axis,
          .extent = extent,
          .margin = margin,
          .title = "librtree-python output"
        };

      int err = rtree_postscript(self->rtree, &postscript, st);

      fclose(st);

      if (err != RTREE_OK)
        return PyErr_Format(PyExc_RuntimeError,
                            "librtree: %s",
                            rtree_strerror(err));
    }

  Py_INCREF(Py_None);
  return Py_None;
}

typedef struct
{
  PyObject *f, *context;
} search_cb_context_t;

static int search_cb(rtree_id_t id, void *varg)
{
  search_cb_context_t *arg = varg;
  PyObject *id_arg = PyLong_FromLong(id);

  if (id_arg == NULL)
    return 1;

  PyObject *cb_arg = PyTuple_Pack(2, id_arg, arg->context);

  Py_DECREF(id_arg);

  if (cb_arg == NULL)
    return 1;

  PyObject *result = PyObject_Call(arg->f, cb_arg, NULL);

  Py_DECREF(cb_arg);

  if (result == NULL)
    return 1;

  long status = PyLong_AsLong(result);

  Py_DECREF(result);

  if ((status == -1) && (PyErr_Occurred()))
    return 1;

  return status;
}

static PyObject*
PyRTree_search(PyRTreeObject *self, PyObject *args)
{
  PyObject
    *f_obj,
    *rect_obj,
    *context_obj;

  if (PyArg_UnpackTuple(args, "search", 3, 3, &f_obj, &rect_obj, &context_obj))
    {
      if (! PyCallable_Check(f_obj))
        return PyErr_Format(PyExc_TypeError, "function not callable");

      if (! PyTuple_Check(rect_obj))
        return PyErr_Format(PyExc_TypeError, "rectangle not a tuple");

      size_t dim = state_dims(self->rtree->state);
      Py_ssize_t len = PyTuple_Size(rect_obj);

      if (len != 2 * (Py_ssize_t)dim)
        return PyErr_Format(PyExc_ValueError, "bad coordinate tuple size %li", len);

      rtree_coord_t coords[2 * dim];

      for (size_t i = 0 ; i < 2 * dim ; i++)
        {
          PyObject *coord_obj = PyTuple_GetItem(rect_obj, i);
          if (coord_obj == NULL)
            return
              PyErr_Format(PyExc_TypeError,
                           "getting element %zi of coordinate");
          if (((coords[i] = PyFloat_AsDouble(coord_obj)) == -1) &&
              (PyErr_Occurred()))
            return PyErr_Format(PyExc_TypeError,
                                "parsing elemment %zi of cccordinate", i);
        }

      search_cb_context_t context = { f_obj, context_obj };

      if (rtree_search(self->rtree, coords, search_cb, &context) != 0)
        return NULL;
    }

  Py_INCREF(Py_None);
  return Py_None;
}

/* serialisation */

typedef int (serialise_t)(const rtree_t*, FILE*);

static PyObject*
serialise(PyRTreeObject *self, PyObject *io_obj, serialise_t *f)
{
  FILE *st;

  if ((st = io_stream(io_obj, "w")) == NULL)
    return NULL;

  int err = f(self->rtree, st);

  fclose(st);

  if (err != RTREE_OK)
    return PyErr_Format(PyExc_RuntimeError,
                        "librtree: %s",
                        rtree_strerror(err));

  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject*
PyRTree_json_write(PyRTreeObject *self, PyObject *io_obj)
{
  return serialise(self, io_obj, rtree_json_write);
}

static PyObject*
PyRTree_bsrt_write(PyRTreeObject *self, PyObject *io_obj)
{
  return serialise(self, io_obj, rtree_bsrt_write);
}

#define PRT_METH(base, args) { #base, (PyCFunction)(PyRTree_ ## base), args, NULL }

static PyMethodDef PyRTree_methods[] =
  {
   PRT_METH(csv_read, METH_VARARGS | METH_CLASS),
   PRT_METH(json_read, METH_O | METH_CLASS),
   PRT_METH(bsrt_read, METH_O | METH_CLASS),
   PRT_METH(size, METH_NOARGS),
   PRT_METH(page_size, METH_NOARGS),
   PRT_METH(node_size, METH_NOARGS),
   PRT_METH(rect_size, METH_NOARGS),
   PRT_METH(branch_size, METH_NOARGS),
   PRT_METH(branching_factor, METH_NOARGS),
   PRT_METH(unit_sphere_volume, METH_NOARGS),
   PRT_METH(dim, METH_NOARGS),
   PRT_METH(height, METH_NOARGS),
   PRT_METH(empty, METH_NOARGS),
   PRT_METH(clone, METH_NOARGS),
   PRT_METH(identical, METH_O),
   PRT_METH(add_rect, METH_VARARGS),
   PRT_METH(search, METH_VARARGS),
   PRT_METH(update, METH_VARARGS),
   PRT_METH(postscript, METH_VARARGS),
   PRT_METH(json_write, METH_O),
   PRT_METH(bsrt_write, METH_O),
   { NULL }
  };

static PyTypeObject PyRTreeType =
  {
   PyVarObject_HEAD_INIT(NULL, 0)
   .tp_name = "librtree.ext.RTree",
   .tp_doc = PyDoc_STR("RTree object"),
   .tp_basicsize = sizeof(PyRTreeObject),
   .tp_itemsize = 0,
   .tp_flags = Py_TPFLAGS_DEFAULT,
   .tp_new = PyRTree_new,
   .tp_init = (initproc)PyRTree_init,
   .tp_dealloc = (destructor)PyRTree_dealloc,
   .tp_methods = PyRTree_methods
  };

/* librtree.ext module */

static struct PyModuleDef ext =
  {
   PyModuleDef_HEAD_INIT,
   .m_name = "ext",
   .m_doc = "The librtree module",
   .m_size = -1,
  };

PyMODINIT_FUNC PyInit_ext(void)
{
  PyObject *mod;

  if ((mod = PyModule_Create(&ext)) == NULL)
    return NULL;

  PyModule_AddStringConstant(mod, "url", rtree_package_url);
  PyModule_AddStringConstant(mod, "bugreport", rtree_package_bugreport);
  PyModule_AddStringConstant(mod, "version", rtree_package_version);

  PyModule_AddIntConstant(mod, "SPLIT_QUADRATIC", RTREE_SPLIT_QUADRATIC);
  PyModule_AddIntConstant(mod, "SPLIT_LINEAR", RTREE_SPLIT_LINEAR);
  PyModule_AddIntConstant(mod, "SPLIT_GREENE", RTREE_SPLIT_GREENE);
  PyModule_AddIntConstant(mod, "AXIS_HEIGHT", axis_height);
  PyModule_AddIntConstant(mod, "AXIS_WIDTH", axis_width);

  if (PyType_Ready(&PyRTreeStyleType) >= 0)
    {
      if (PyType_Ready(&PyRTreeType) >= 0)
        {
          if (PyModule_AddObject(mod, "RTreeStyle", (PyObject*)&PyRTreeStyleType) >= 0)
            {
              if (PyModule_AddObject(mod, "RTree", (PyObject*)&PyRTreeType) >= 0)
                return mod;

              Py_INCREF(&PyRTreeType);
            }
          Py_INCREF(&PyRTreeStyleType);
        }
    }

  Py_DECREF(mod);
  return NULL;
}
