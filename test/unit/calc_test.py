import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True

def mocked_validation_false(*args, **kwargs):
    return False


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
    
    # Pruebas para el método add (suma)
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
    
    # Pruebas para el método substract (resta)
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(5, self.calc.substract(10, 5))
        self.assertEqual(-7, self.calc.substract(-2, 5))
        self.assertEqual(2, self.calc.substract(2, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)

    # Pruebas para el método divide (division)
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(3.4, self.calc.divide(3.4, 1))
        self.assertEqual(-4, self.calc.divide(-8, 2))
        self.assertEqual(6, self.calc.divide(-24, -4))
        
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)
        
    # Pruebas adicionales para `divide` con números flotantes
    def test_divide_method_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1e-10, 1e-5), 1e-5)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
    
    # Pruebas para el método multiply (multiplicacion)  
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply,"2", 2)
        self.assertRaises(TypeError, self.calc.multiply,1, "0")
        self.assertRaises(TypeError, self.calc.multiply,None, 0)
        self.assertRaises(TypeError, self.calc.multiply,-1, None)
        
    @patch('app.util.validate_permissions', side_effect=mocked_validation_false, create=True)
    def test_multiply_method_fails_due_to_invalid_permissions(self, _validate_permissions):
        with self.assertRaises(InvalidPermissions):
            self.calc.multiply(3, 4)
        
    # Pruebas para el método sqrt (raíz cuadrada)
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.sqrt(16))
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertEqual(5, self.calc.sqrt(25))

    def test_sqrt_method_fails_with_negative_number(self):
        self.assertRaises(TypeError , self.calc.sqrt, -4)
        self.assertRaises(TypeError, self.calc.sqrt, -1)

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "16")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        
    def test_sqrt_method_with_small_float(self):
        self.assertAlmostEqual(self.calc.sqrt(1e-10), 1e-5)

    # Pruebas para el método log10 (logaritmo base 10)
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(2.0, self.calc.log10(100))
        self.assertEqual(1.0, self.calc.log10(10))
        self.assertEqual(0.0, self.calc.log10(1))
        self.calc.log10(1e-50)

    # Pruebas para el método log10 (logaritmo base 10) error
    def test_log10_method_fails_with_non_positive_number(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -10)
        
    # Pruebas para el método power (potencia)
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "100", 2)
        self.assertRaises(TypeError, self.calc.power, "100", "2")
        self.assertRaises(TypeError, self.calc.power, None, None)
        self.assertRaises(TypeError, self.calc.power, None, 4)
    
    # Pruebas para el método power (potencia) valores correctos
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(9, self.calc.power(3, 2))
        self.assertEqual(3.4, self.calc.power(3.4, 1))
        self.assertEqual(4096, self.calc.power(-8, 4))
        
    # Pruebas para el método check_types (verifica ambos parametros)
    def test_check_types_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_types, "100", 2)
        self.assertRaises(TypeError, self.calc.check_types, 100, "2")
        self.assertRaises(TypeError, self.calc.check_types, "100", "2")
        self.assertRaises(TypeError, self.calc.check_types, None, None)
        self.assertRaises(TypeError, self.calc.check_types, None, 4)
    
    # Pruebas para el método check_types resultados correctos
    def test_check_types_method_returns_correct_result(self):
        self.calc.check_types(2, 2)
        self.calc.check_types(-3, -2)
        self.calc.check_types(3.4, 1)
        self.calc.check_types(8.2, 2.3)
    
    # Pruebas para check_types con float('inf') y float('nan')
    def test_check_types_with_special_floats(self):
        self.assertRaises(TypeError, self.calc.check_types, float('nan'), 2)
        self.assertRaises(TypeError, self.calc.check_types, 2, float('nan'))
        self.assertRaises(TypeError, self.calc.check_types, float('inf'), None)
        self.assertRaises(TypeError, self.calc.check_types, None, float('inf'))
        
    # Pruebas para el método check_single_type (verifica un parametro)
    def test_check_single_type_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_single_type, "100")
        self.assertRaises(TypeError, self.calc.check_single_type, 100,8)
        self.assertRaises(TypeError, self.calc.check_single_type, None)
    
    # Pruebas para el metodo check_single_types resultados correctos
    def test_check_single_type_method_returns_correct_result(self):
        self.calc.check_single_type(3)
        self.calc.check_single_type(3.4)
        self.calc.check_single_type(-2)
        
    # Pruebas para el metodo check_single_types float('inf') y float('nan')       
    def test_check_single_type_with_special_floats(self):
        self.assertRaises(TypeError, self.calc.check_single_type, float('nan'))
        self.assertRaises(TypeError, self.calc.check_single_type, float('inf'))

    

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
