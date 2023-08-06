//
//MIT License
//Copyright (c) 2023 JeongHan-Bae
//Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
//The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
//
#include <Python.h>
#include <malloc.h>
#include <stdbool.h>
/*les fonctions basiques*/
bool is_deck(const int* p, int n) {
    bool* count =(bool *) calloc(n, sizeof(bool));
    for (int i = 0; i < n; i++) {
        if (*(p+i) < 1 || *(p+i) > n) {
            return false;
        }
        *(count + *(p + i) - 1) = true;
    }
    for (int i = 0; i < n; i++) {
        if (!*(count + i)) {
            free(count);
            return false;
        }
    }
    free(count);
    return true;
}
bool is_init(const int* p,int n){
    for (int i = 0; i < n; i++) {
        if (*(p+i)!=i+1){
            return false;
        }
    }
    return true;
}
int orbit(const int* m,int n){
    int orb=0;
    int* cards = (int *) malloc(n * sizeof(int));
    int* temp = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        *(cards+i)=i+1;
    }
    bool back = false;
    bool t_bool;
    while (!back){
        for (int i = 0; i < n; i++) {
            *(temp+i)=*(cards+*(m+i)-1);
        }
        orb++;
        t_bool = true;
        for (int i = 0; i < n; i++) {
            *(cards+i)=*(temp+i);
            if (*(temp+i)!=i+1){
                t_bool= false;
            }
        }
        back=t_bool;
    }
    free(cards);
    free(temp);
    return orb;
}
int* shuffle(const int* p, const int* m, int n){
    int* cards = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        *(cards+i)=*(p+*(m+i)-1);
    }
    return cards;
}
int* reverse(const int* m,int n){
    int* cards = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        *(cards+*(m+i)-1)=i+1;
    }
    return cards;
}
int* cycle(const int* m, int n, int k){
    int* cards = (int *) malloc(n * sizeof(int));
    int* temp = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        *(cards+i)=i+1;
    }
    for (int turn=0;turn<k;turn++){
        for (int i = 0; i < n; i++) {
            *(temp+i)=*(cards+*(m+i)-1);
        }
        for (int i = 0; i < n; i++) {
            *(cards+i)=*(temp+i);
        }
    }
    free(temp);
    return cards;
}
int* rev_cycle(const int* m, int n, int k){
    int* cards = (int *) malloc(n * sizeof(int));
    int* temp = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        *(cards+i)=i+1;
    }
    for (int turn=0;turn<k;turn++){
        for (int i = 0; i < n; i++) {
            *(temp+*(m+i)-1)=*(cards+i);
        }
        for (int i = 0; i < n; i++) {
            *(cards+i)=*(temp+i);
        }
    }
    free(temp);
    return cards;
}

static PyObject* is_deck_wrapper(PyObject* self, PyObject* args) {
    PyObject* pack_obj;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "O", &pack_obj)) {
        return NULL;
    }
    // Vérifier que l'objet passé est une liste Python
    if (!PyList_Check(pack_obj)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list of integers");
        return NULL;
    }
    // Convertir la liste Python en tableau C int
    int n = PyList_Size(pack_obj);
    int* pack = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject* item = PyList_GetItem(pack_obj, i);
        if (!PyLong_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "Expected a list of integers");
            free(pack);
            return NULL;
        }
        *(pack+i) = PyLong_AsLong(item);
    }
    // Appeler la fonction is_deck basique
    bool result = is_deck(pack, n);
    free(pack);
    // Retourner le résultat en tant qu'objet Python
    if (result) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}
static PyObject* is_init_wrapper(PyObject* self, PyObject* args) {
    PyObject* pack_obj;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "O", &pack_obj)) {
        return NULL;
    }
    // Vérification que pack_obj est une liste
    if (!PyList_Check(pack_obj)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list");
        return NULL;
    }
    // Récupération des valeurs de la liste pack_obj
    int n = PyList_Size(pack_obj);
    int* p = (int*)malloc(n * sizeof(int));
    if (p == NULL) {
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for pack_obj");
        return NULL;
    }
    for (int i = 0; i < n; i++) {
        PyObject* item = PyList_GetItem(pack_obj, i);
        *(p+i) = (int)PyLong_AsLong(item);
    }
    // Appel à la fonction is_init basique
    bool is_init_result = is_init(p, n);
    free(p);
    // Conversion du résultat en Python booléen
    if (is_init_result) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}
static PyObject* orbit_wrapper(PyObject* self, PyObject* args) {
    PyObject* shuffle_obj;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "O", &shuffle_obj)) {
        return NULL;
    }
    // Vérifier que l'objet passé est une liste Python
    if (!PyList_Check(shuffle_obj)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list of integers");
        return NULL;
    }
    // Convertir la liste Python en tableau C int
    int n = PyList_Size(shuffle_obj);
    int* m = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject* item = PyList_GetItem(shuffle_obj, i);
        if (!PyLong_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "Expected a list of integers");
            free(m);
            return NULL;
        }
        *(m+i) = PyLong_AsLong(item);
    }
    // Vérifier que le tableau m : est un paquet de cartes
    if (!is_deck(m, n)) {
        PyErr_SetString(PyExc_TypeError, "Not a pack");
        free(m);
        return NULL;
    }
    // Appeler la fonction orbit basique
    int result = orbit(m, n);
    free(m);
    // Retourner le résultat en tant qu'objet Python
    return PyLong_FromLong(result);
}
static PyObject* shuffle_wrapper(PyObject* self, PyObject* args) {
    PyObject* pack_obj;
    PyObject* shuffle_obj;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "OO", &pack_obj, &shuffle_obj)) {
        return NULL;
    }
    // Vérifier que les objets passés sont des listes Python
    if (!PyList_Check(pack_obj)) {
        PyErr_SetString(PyExc_TypeError, "The first variable should be a list of integers");
        return NULL;
    }
    if (!PyList_Check(shuffle_obj)) {
        PyErr_SetString(PyExc_TypeError, "The second variable should be a list of integers");
        return NULL;
    }
    // Convertir les listes Python en tableaux C int
    int n = PyList_Size(pack_obj);
    if (n != PyList_Size(shuffle_obj)) {
        PyErr_SetString(PyExc_TypeError, "The two variables should have the same length");
        return NULL;
    }
    int* pack = malloc(n * sizeof(int));
    int* shuffle_method = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject* item1 = PyList_GetItem(pack_obj, i);
        PyObject* item2 = PyList_GetItem(shuffle_obj, i);
        if (!PyLong_Check(item1)) {
            PyErr_SetString(PyExc_TypeError, "The first variable should be a list of integers");
            free(pack);
            free(shuffle_method);
            return NULL;
        }
        if (!PyLong_Check(item2)) {
            PyErr_SetString(PyExc_TypeError, "The second variable should be a list of integers");
            free(pack);
            free(shuffle_method);
            return NULL;
        }
        *(pack+i) = PyLong_AsLong(item1);
        *(shuffle_method + i) = PyLong_AsLong(item2);
    }
    // Vérifier que la variable pack est un paquet de cartes
    if (!is_deck(pack, n)) {
        PyErr_SetString(PyExc_TypeError, "The first variable should be a pack");
        free(pack);
        free(shuffle_method);
        return NULL;
    }
    // Vérifier que la variable shuffle_method est un paquet de cartes
    if (!is_deck(shuffle_method, n)) {
        PyErr_SetString(PyExc_TypeError, "The second variable should be a pack");
        free(pack);
        free(shuffle_method);
        return NULL;
    }
    // Appeler la fonction shuffle basique
    int* res = shuffle(pack, shuffle_method, n);
    free(pack);
    free(shuffle_method);
    // Créer la liste Python qui va contenir le résultat
    PyObject* result = PyList_New(n);
    if (result == NULL) {
        free(res);
        return NULL;
    }
    // Copier le résultat dans la liste Python
    for (int i = 0; i < n; i++) {
        PyObject* item = PyLong_FromLong(*(res+i));
        if (item == NULL) {
            Py_DECREF(result);
            free(res);
            return NULL;
        }
        PyList_SET_ITEM(result, i, item);
    }
    free(res);
    // Retourner la liste Python contenant le résultat
    return result;
}
static PyObject* reverse_shuffle_wrapper(PyObject* self, PyObject* args) {
    PyObject* shuffle_obj;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "O", &shuffle_obj)) {
        return NULL;
    }
    // Vérifier que l'objet passé est une liste Python
    if (!PyList_Check(shuffle_obj)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list of integers");
        return NULL;
    }
    // Convertir la liste Python en tableau C int
    int n = PyList_Size(shuffle_obj);
    int* shuffle = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject* item = PyList_GetItem(shuffle_obj, i);
        if (!PyLong_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "Expected a list of integers");
            free(shuffle);
            return NULL;
        }
        *(shuffle+i) = PyLong_AsLong(item);
    }
    // Vérifier que la liste passée est un paquet de cartes
    if (!is_deck(shuffle, n)) {
        PyErr_SetString(PyExc_TypeError, "Not a pack");
        free(shuffle);
        return NULL;
    }
    // Appeler la fonction reverse basique
    int* res = reverse(shuffle, n);
    // Créer une liste Python pour stocker les résultats
    PyObject* result = PyList_New(n);
    if (!result) {
        free(shuffle);
        free(res);
        return NULL;
    }
    // Convertir le tableau C en liste Python
    for (int i = 0; i < n; i++) {
        PyObject* item = PyLong_FromLong(*(res+i));
        if (!item) {
            free(shuffle);
            free(res);
            Py_DECREF(result);
            return NULL;
        }
        PyList_SET_ITEM(result, i, item);
    }
    free(shuffle);
    free(res);
    // Retourner le résultat en tant qu'objet Python
    return result;
}
static PyObject* cycle_wrapper(PyObject* self, PyObject* args) {
    PyObject *shuffle_obj;
    int k;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "Oi", &shuffle_obj, &k)) {
        return NULL;
    }
    if (!PyList_Check(shuffle_obj)) {
        PyErr_SetString(PyExc_TypeError, "First argument must be a list.");
        return NULL;
    }
    int n = PyList_Size(shuffle_obj);
    int *m = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject *item = PyList_GetItem(shuffle_obj, i);
        if (!PyLong_Check(item)) {
            free(m);
            PyErr_SetString(PyExc_TypeError, "Elements of the list must be integers.");
            return NULL;
        }
        *(m+i) = (int) PyLong_AsLong(item);
    }
    if (!is_deck(m, n)) {
        free(m);
        PyErr_SetString(PyExc_TypeError, "Not a pack");
        return NULL;
    }
    int *res;
    if (k >= 0) {
        res = cycle(m, n, k);
    } else {
        res = rev_cycle(m, n, -k);
    }
    PyObject *result = PyList_New(n);
    for (int i = 0; i < n; i++) {
        PyList_SetItem(result, i, PyLong_FromLong(*(res+i)));
    }
    free(m);
    free(res);
    return result;
}
static PyObject* rev_cycle_wrapper(PyObject* self, PyObject* args) {
    PyObject *shuffle_obj;
    int k;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "Oi", &shuffle_obj, &k)) {
        return NULL;
    }
    if (!PyList_Check(shuffle_obj)) {
        PyErr_SetString(PyExc_TypeError, "First argument must be a list.");
        return NULL;
    }
    int n = PyList_Size(shuffle_obj);
    int *m = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject *item = PyList_GetItem(shuffle_obj, i);
        if (!PyLong_Check(item)) {
            free(m);
            PyErr_SetString(PyExc_TypeError, "Elements of the list must be integers.");
            return NULL;
        }
        *(m+i) = (int) PyLong_AsLong(item);
    }
    if (!is_deck(m, n)) {
        free(m);
        PyErr_SetString(PyExc_TypeError, "Not a pack");
        return NULL;
    }
    int *res;
    if (k >= 0) {
        res = rev_cycle(m, n, k);
    } else {
        res = cycle(m, n, -k);
    }
    PyObject *result = PyList_New(n);
    for (int i = 0; i < n; i++) {
        PyList_SetItem(result, i, PyLong_FromLong(*(res+i)));
    }
    free(m);
    free(res);
    return result;
}
static PyObject* all_cases(PyObject* self, PyObject* args) {
    PyObject* shuffle_obj;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "O", &shuffle_obj)) {
        return NULL;
    }
    if (!PyList_Check(shuffle_obj)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a list");
        return NULL;
    }
    int n = PyList_Size(shuffle_obj);
    int *m = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject* item = PyList_GetItem(shuffle_obj, i);
        if (!PyLong_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "List must contain integers only");
            return NULL;
        }
        *(m+i) = PyLong_AsLong(item);
    }
    if (!is_deck(m, n)) {
        PyErr_SetString(PyExc_TypeError, "Not a pack");
        return NULL;
    }
    int k = orbit(m, n);
    PyObject* result = PyList_New(k);
    for (int i = 0; i < k - 1; i++) {
        int* case_m = cycle(m, n, i + 1);
        PyObject* case_py = PyList_New(n);
        for (int j = 0; j < n; j++) {
            PyList_SetItem(case_py, j, PyLong_FromLong(*(case_m+j)));
        }
        PyList_SetItem(result, i, case_py);
        free(case_m);
    }
    PyObject* init = PyList_New(n);
    for (int i = 0; i < n; i++) {
        PyList_SetItem(init, i, PyLong_FromLong(i + 1));
    }
    PyList_SetItem(result, k - 1, init);
    return result;
}
static PyObject* find_shuffle(PyObject* self, PyObject* args) {
    PyObject* pack0_obj;
    PyObject* pack1_obj;
    // Analyser les arguments passés depuis Python
    if (!PyArg_ParseTuple(args, "OO", &pack0_obj, &pack1_obj)) {
        return NULL;
    }
    // Vérifier que les objets passés sont des listes Python
    if (!PyList_Check(pack0_obj)) {
        PyErr_SetString(PyExc_TypeError, "The first variable should be a list of integers");
        return NULL;
    }
    if (!PyList_Check(pack1_obj)) {
        PyErr_SetString(PyExc_TypeError, "The second variable should be a list of integers");
        return NULL;
    }
    // Convertir les listes Python en tableaux C int
    int n = PyList_Size(pack0_obj);
    if (n != PyList_Size(pack1_obj)) {
        PyErr_SetString(PyExc_TypeError, "The two variables should have the same length");
        return NULL;
    }
    int* pack0 = malloc(n * sizeof(int));
    int* pack1 = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        PyObject* item1 = PyList_GetItem(pack0_obj, i);
        PyObject* item2 = PyList_GetItem(pack1_obj, i);
        if (!PyLong_Check(item1)) {
            PyErr_SetString(PyExc_TypeError, "The first variable should be a list of integers");
            free(pack0);
            free(pack1);
            return NULL;
        }
        if (!PyLong_Check(item2)) {
            PyErr_SetString(PyExc_TypeError, "The second variable should be a list of integers");
            free(pack0);
            free(pack1);
            return NULL;
        }
        *(pack0 + i) = PyLong_AsLong(item1);
        *(pack1 + i) = PyLong_AsLong(item2);
    }
    // Vérifier que pack0 est un paquet de cartes
    if (!is_deck(pack0, n)) {
        PyErr_SetString(PyExc_TypeError, "The first variable should be a pack");
        free(pack0);
        free(pack1);
        return NULL;
    }
    if (!is_deck(pack1, n)) {
        PyErr_SetString(PyExc_TypeError, "The second variable should be a pack");
        free(pack0);
        free(pack1);
        return NULL;
    }
    // Appeler les fonctions basiques
    int* res = reverse(shuffle(reverse(pack1, n), pack0, n), n);
    free(pack0);
    free(pack1);
    // Créer la liste Python qui va contenir le résultat
    PyObject* result = PyList_New(n);
    if (result == NULL) {
        free(res);
        return NULL;
    }
    // Copier le résultat dans la liste Python
    for (int i = 0; i < n; i++) {
        PyObject* item = PyLong_FromLong(*(res+i));
        if (item == NULL) {
            Py_DECREF(result);
            free(res);
            return NULL;
        }
        PyList_SET_ITEM(result, i, item);
    }
    free(res);
    // Retourner la liste Python contenant le résultat
    return result;
}
static PyObject* pack_init(PyObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }
    PyObject* result = PyList_New(n);
    if (!result) {
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for result");
        return NULL;
    }
    for (int i = 0; i < n; i++) {
        PyObject* item = PyLong_FromLong(i + 1);
        if (!item) {
            Py_DECREF(result);
            PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory for item");
            return NULL;
        }
        PyList_SET_ITEM(result, i, item);
    }
    return result;
}
static PyObject* orbitmagic_help(PyObject* self, PyObject* args) {
    PyObject* dict_obj = PyModule_GetDict(self);
    PyObject* keys_list = PyDict_Keys(dict_obj);
    PyObject* key_obj;
    Py_ssize_t i, len = PyList_Size(keys_list);
    printf("\033[0m\033[1m\033[3m\033[32mHello Magician, Welcome!\n\033[0m\033[1m\033[36m-- JH Bae\n\033[0m\033[1mcontact us : \033[4mhttps://github.com/JeongHan-Bae\n\033[0m\033[1mThe library functions are as follows :\033[0m\n");
    for (i = 0; i < len; i++) {
        key_obj = PyList_GetItem(keys_list, i);
        const char* name = PyUnicode_AsUTF8(key_obj);
        PyObject* item_obj = PyDict_GetItemString(dict_obj, name);
        if (item_obj && PyCFunction_Check(item_obj)) {
            PyCFunctionObject* func = (PyCFunctionObject*) item_obj;
            PyMethodDef* method = func->m_ml;
            if (method && method->ml_doc && strcmp(method->ml_name, "help") != 0){
                printf("\033[0m%s : %s\033[0m\n", method->ml_name, method->ml_doc);
            }
        }
    }
    printf("\033[0m\033[1mIf you want to get more detailed information, please check the attached files.\033[0m\n");
    Py_DECREF(keys_list);
    Py_RETURN_NONE;
}

// Liste des méthodes exposées par le module
static PyMethodDef module_methods[] = {
        {"is_deck",   is_deck_wrapper,         METH_VARARGS, "Check if a list of integers is a deck."},
        {"is_init",   is_init_wrapper,         METH_VARARGS, "Check if a list of integers is the initial deck."},
        {"orbit",     orbit_wrapper,           METH_VARARGS, "Calculate the orbit of a shuffle."},
        {"shuffle",   shuffle_wrapper,         METH_VARARGS, "Shuffle a pack with a certain method."},
        {"reverse",   reverse_shuffle_wrapper, METH_VARARGS, "Reversing a shuffle."},
        {"cycle",     cycle_wrapper,           METH_VARARGS, "Calculate an iterative loop of a shuffle."},
        {"rev_cycle", rev_cycle_wrapper,       METH_VARARGS, "Calculate a reverse loop of a shuffle."},
        {"all_cases", all_cases,               METH_VARARGS, "Calculate all iterations of a shuffle."},
        {"find_shuffle",  find_shuffle,                METH_VARARGS, "Find the shuffling method."},
        {"pack_init", pack_init,               METH_VARARGS, "Give the initial deck of cards."},
        {"help",      orbitmagic_help,         METH_VARARGS, "Display help for this module."},
        {NULL, NULL, 0, NULL}
};

// Initialisation du module
static PyModuleDef OrbitMagicModule = {
        PyModuleDef_HEAD_INIT,
        "orbitmagic",
        "A module that helps magicians to model mathematical orbits and helps with encrypting.",
        -1,
        module_methods
        };
PyMODINIT_FUNC PyInit_orbitmagic(void) {
    return PyModule_Create(&OrbitMagicModule);
}