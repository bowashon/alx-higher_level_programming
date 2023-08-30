#include <Python.h>
/**
 * print_python_list_info - function that prints basic information
 * about pythyon
 * @p: pointer to pyobject lists
 *
 */
void print_python_list_info(PyObject *p)
{
	int len, element, i;
	PyObject *object;

	len = Py_SIZE (p);
	element = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", len);
	printf("[*] Allocated = %d\n", element);

	for (i = 0; i < len; i++)
	{
		object = PyList_GetItem(p, i);
		printf("Element %d: ", i)
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
