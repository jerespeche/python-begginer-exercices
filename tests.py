import unittest

import exercises

# class AddTestCase(unittest.TestCase):

#     def test_adds_correctly(self):
#         """
#         Deberia devolver la suma de los numeros.
#         """
#         result = exercises.add(5, 3)

#         self.assertEqual(8, result)

# class MultiplyTestCase(unittest.TestCase):

#     def test_multiplies_correctly(self):
#         """
#         Deberia devolver la multiplicacion de los numeros.
#         """
#         result = exercises.multiply(5, 3)

#         self.assertEqual(15, result)

# class CelciusToFarenheitTestCase(unittest.TestCase):

#     def test_calculates_correctly(self):
#         result = exercises.celsius_to_farenheit(32.4)

#         self.assertEqual(90.32, result)

# class CreatePersonTestCase(unittest.TestCase):
#     def setUp(self):
#         self.result = exercises.create_person("Juan", "Calabera", "Desempleado")

#     def test_returns_a_dict(self):
#         """
#         Deberia devolver un dict.
#         """
#         self.assertIsInstance(self.result, dict)

#     def test_has_correct_name(self):
#         """
#         Deberia tener el nombre asignado correctamente
#         """
#         self.assertEqual("Juan",self.result["name"])

#     def test_has_correct_last_name(self):
#         """
#         Deberia tener el apellido asignado correctamente
#         """
#         self.assertEqual("Calabera",self.result["last_name"])

#     def test_has_correct_job(self):
#         """
#         Deberia tener el trabajo asignado correctamente
#         """
#         self.assertEqual("Desempleado",self.result["job"])

class GreetTestCase(unittest.TestCase):
    def test_should_return_greet_correctly(self):
        data = {"name": "John", "last_name": "Martinez"}

        result = exercises.greet(data)

        self.assertEqual("Hola, me llamo John Martinez", result)

# class IsOverAgeTestCase(unittest.TestCase):
    
#     def test_detects_underage(self):
#         """
#         Deberia devolver False si la persona es menor de edad.
#         """
#         result = exercises.is_overage(15)

#         self.assertFalse(result)

#     def test_true_when_overage(self):
#         """
#         Deberia devolver True si la persona es mayor de edad.
#         """
#         result = exercises.is_overage(25)

#         self.assertTrue(result)

#     def test_true_when_is_18(self):
#         """
#         Deberia devolver True si la persona tiene 18.
#         """
#         result = exercises.is_overage(18)

#         self.assertTrue(result)

# class FooBarTestCase(unittest.TestCase):
#     def test_foo_when_multiple_of_three(self):
#         """
#         Deberia devolver 'foo' cuando el numero es multiplo de 3.
#         """
#         data = 9
        
#         result = exercises.foo_bar(data)

#         self.assertEqual('foo', result)

#     def test_bar_when_multiple_of_five(self):
#         """
#         Deberia devolver 'bar' cuando el numero es multiplo de 5.
#         """
#         data = 20
        
#         result = exercises.foo_bar(data)

#         self.assertEqual('bar', result)


#     def test_foobar_when_multiple_of_three_and_five(self):
#         """
#         Deberia devolver 'foobar' cuando el numero es multiplo de 3 y de 5.
#         """
#         data = 30
        
#         result = exercises.foo_bar(data)

#         self.assertEqual('foobar', result)
    
# class AddNumbersTestCase(unittest.TestCase):
#     def test_adds_numbers_correctly(self):
#         """
#         Deberia agregar los numeros de la lista correctamente
#         """
#         data = [1,3,5]

#         result = exercises.add_numbers(data)

#         self.assertEqual(9, result)

#     def test_also_works_with_negatives(self):
#         """
#         Deberia funcionar con numeros negativos tambien
#         """
#         data = [1,-3,5]

#         result = exercises.add_numbers(data)
#         self.assertEqual(3, result)

# class AddGreetingsToNamesTestCase(unittest.TestCase):
#     def setUp(self):
#         data = ["Paula", "Marcos", "Sofia"]
#         self.result = exercises.add_greetings_to_names(data)

#     def test_returns_a_list(self):
#         """
#         Deberia devolver una lista.
#         """
#         self.assertIsInstance(self.result, list)

#     def test_returns_correct_greetings(self):
#         """
#         Deberia devolver una lista con las presentaciones de cada uno.
#         """
#         correct_results = ['Hola, me llamo Paula', 'Hola, me llamo Marcos', 'Hola, me llamo Sofia']
#         self.assertEqual(correct_results, self.result)

if __name__ == '__main__':
    unittest.main()