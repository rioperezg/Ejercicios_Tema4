"""
Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla –para lo cual deberá calcular 
primero las frecuencias de cada carácter a partir de la can- tidad de apariciones del mismo–, para resolver las siguientes actividades:

 

A.la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres 
tengan la misma frecuencia, primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran 
anteúltimo y último respectivamente en el orden alfabético;
 

B.descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
 

I.   Mensaje  1:  “100010111010110000101110100011100000110110000001111001111010010110

0001101001110011010001011101011111110100001111001111110011110100011000110000

00101101011110111111101110101101101110011101101111001111111001010010100101000001

011010110001011001101000111001001011000011001000110101101010111111111110110111

0111001000010010101100011111110001000111011001100101101000110111110101101000

1101110000000111001001010100011111100001100101101011100110011110100011000110

000001011010111110011100”

 

II.    Mensaje 2: “01101010110111001010001111010111001101110101101101000010001110101001

011110100111111101110010100011110101110011011101011000011000100110100011100100

10001100010110011001110010010000111101111010”

 

C.finalmente, calcule el espacio de memoria requerido por el mensaje original y el comprimido.
"""