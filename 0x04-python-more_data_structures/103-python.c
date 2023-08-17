#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints info about a Python lists.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t list_size = PyList_Size(p);
		Py_ssize_t i = 0;
		PyObject *item = PyList_GetItem(p, i);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", list_size);
		printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < list_size; i++)
		{
			printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Python List Object\n");
	}
}

/**
 * print_python_bytes - Prints info about a Pyobject.
 * @p: Points to the Pyobject struct.
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t list_size = PyBytes_Size(p);

		printf("[.] bytes object info\n");
		printf("        size: %zd\n", list_size);
		printf("  trying string: %s\n", PyBytes_AsString(p));

		printf("  first %zd bytes: ", (list_size > 10) ? 10 : list_size);
		for (Py_ssize_t i = 0; i < ((list_size > 10) ? 10 : list_size); i++)
		{
			printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
			if (i < 9 && i < list_size - 1)
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid PyBytes Object\n");
	}
}
