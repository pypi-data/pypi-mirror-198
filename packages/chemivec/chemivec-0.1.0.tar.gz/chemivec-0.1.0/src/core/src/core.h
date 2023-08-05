//
// Created by ergot on 09/03/2023.
//

#ifndef CHEMIVEC_VEC_H
#define CHEMIVEC_VEC_H
#endif //CHEMIVEC_VEC_H

#include "Python.h"
#include "indigo.h"
#include <omp.h>

#define PY_ARRAY_UNIQUE_SYMBOL CHEMIVEC_ARRAY_API
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/arrayobject.h"

typedef struct {
    qword sid;
    int num_cores;
} ChemivecOptions;

typedef struct {
    char** pinput;
    npy_bool* poutput;
    int size;
    qword sid;
    int threadid;
} ReactionBatch;

PyArrayObject* cstr2numpy(char** strings, int size);

char** numpy2cstr(PyArrayObject * np_array);

void reactionMatchBatch(ReactionBatch* batch, int query, const char *mode);

void reactionMatchLin(char **in_data, npy_bool *out_data, int size, char *querySmarts, const char *mode);

void reactionMatchVec(char **in_data, npy_bool *out_data, int size, char *querySmarts, const char *mode, int numCores);

PyArrayObject *
reactionMatchNumPy(PyArrayObject *np_input, char *querySmarts, char *aamMode, int numCores, ChemivecOptions *options);


inline static void finishSearch(int rxn, int matcher, int match) {
    indigoFree(rxn);
    indigoFree(matcher);
    indigoFree(match);
}


