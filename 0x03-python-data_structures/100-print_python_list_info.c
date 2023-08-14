#include <Python.h>
#include <object.h>
#include <listobject.h>

/*
* print_python_list_info - 
* @p:
*
* Return:
*/
void print_python_list_info(PyObject *p)
{
    Py_ssize_t index;
    Py_ssize_t list_size;
    PyObject *item;

    list_size = PyList_Size(p)

    printf("[*] Size of the Python List = %ld\n",size)
    printf("[*] Allocated = %ld\n",((PyListObject *)p)->allocated);

    for (index = 0; index < size; index++)
    {
        item = PyList_GetItem(p, index);
        printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
    }
}
