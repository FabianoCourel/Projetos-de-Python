def escreva(txt):
    print('\033[33m-\033[m' * len(txt))
    print(txt)
    print('\033[33m-\033[m' * len(txt))


escreva('   Courel   ')
escreva('   Curso de Python   ')
escreva('   Curso em Video   ')