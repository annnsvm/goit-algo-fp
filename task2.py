import turtle


# Рекурсивна функція для дерева Піфагора
def pifagorian_tree(t, deepth, size, angle):
    if deepth == 0:
        t.backward(size/0.8)
    else:
        t.right(angle)
        t.forward(size)
        pifagorian_tree(t, deepth - 1, size*0.8, angle)
        t.left(angle*2)
        t.forward(size)
        pifagorian_tree(t, deepth - 1, size*0.8, angle)
        t.right(angle)
        t.backward(size/0.8)


# Функція малювання дерева за допомогою модулю Turtle
def draw_pifagorian_tree(deepth):
    window = turtle.Screen()
    window.bgcolor("white")
    size = 128
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.left(90)
    t.forward(size)
    t.pendown()
    pifagorian_tree(t, deepth, size, 45)
    window.mainloop()


# Запит у користувача числа для побудови дерева Піфагора
def main():
    user_input = input('Введіть ціле число від 1 до 10: ')
    user_input = int(user_input)
    if user_input > 0 and user_input < 11:
        draw_pifagorian_tree(user_input)
    else:
        print('Invalid command.')


if __name__ == "__main__":
    main()