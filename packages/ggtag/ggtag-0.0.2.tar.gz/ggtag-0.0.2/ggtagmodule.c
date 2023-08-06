#define PY_SSIZE_T_CLEAN
#include <Python.h>

uint8_t* encode(const char *input, int *length);

static PyObject *method_encode(PyObject *self, PyObject *args) {
    const char *str;

    if (!PyArg_ParseTuple(args, "s", &str)) {
        return NULL;
    }
    int n;
    uint8_t* buff = encode(str, &n);
    Py_ssize_t buff_size = n;
    PyObject* result = Py_BuildValue("y#", buff, buff_size);
    free(buff);
    return result;
}

static PyMethodDef EncodeMethods[] = {
    {"encode", method_encode, METH_VARARGS, "Encode a string"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef ggtagmodule = {
    PyModuleDef_HEAD_INIT,
    "ggtag",
    "Python interface for ggtag",
    -1,
    EncodeMethods
};

PyMODINIT_FUNC PyInit_ggtag(void) {
    return PyModule_Create(&ggtagmodule);
}