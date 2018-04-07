
#include <boost/python.hpp>
#include <iostream>

template <typename T>
const T power(T base, T exponent) {

    T local_base = base;

    if (exponent == 0) return 1;

    for (;exponent > 1;--exponent) {
        local_base = local_base * base;
    }

    return local_base;
}

BOOST_PYTHON_MODULE(example) {

    using namespace boost::python;

    def("ipower", power<int>,    args("base", "exponent"));
    def("fpower", power<float>,  args("base", "exponent"));
    def("dpower", power<double>, args("base", "exponent"));
    
}
