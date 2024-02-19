import turtle


class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom  # инициатор
        self.state = axiom  # строка с набором команд для фрактала (вначале это инициатор)
        self.width = width  # толщина линии рисования
        self.length = length  # длина одного линейного сегмента кривой
        self.angle = angle  # фиксированный угол поворота
        self.t = t  # сама черепашка
        self.rules = {}  # словарь для хранения правил формирования кривых
        self.t.pensize(self.width)

    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def set_turtle(self, my_tuple):
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()

    def draw_turtle(self, start_pos, start_angle):
        # ***************
        turtle.tracer(1, 0)  # форсажный режим для черепашки
        self.t.up()  # черепашка воспаряет над поверхностью (чтобы не было следа)
        self.t.setpos(start_pos)  # начальная стартовая позиция
        self.t.seth(start_angle)  # начальный угол поворота
        self.t.down()  # черепашка опускается на "грешную землю"
        turtle_stack = []
        # ***************
        for move in self.state:
            if move == 'F':
                self.t.forward(self.length)
            elif move == 'B':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == 'S':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)
            elif move == "[":
                turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize()))
            elif move == "]":
                xcor, ycor, head, w = turtle_stack.pop()
                self.set_turtle((xcor, ycor, head))
                self.width = w
                self.t.pensize(self.width)

        turtle.done()  # чтобы окно не закрывалось после отрисовки


# ************** чтобы окно появлялось в левом верхнем углу с размерами 1200x600
width = 600
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
# **************
t = turtle.Turtle()
#t.ht()  # скрываем черепашку

pen_width = 1  # толщина линии рисования (в пикселах)
f_len = 10  # длина одного сегмента прямой (в пикселах)

# Ефанов Иван Николаевич	7 — 11	3
#
# #7. Мозаика Хагерти
# axiom = "F-F-F-F"
# angle = 180 / 2
# l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F – B + F – F – F – FB – F + B – F + F + F + FB + FF"), ("B", "BBBB"))
# l_sys.generate_path(2)
# print(l_sys.state)
# l_sys.draw_turtle((0, -200), 0)
#
# # 8. Остров
# axiom = "F - F - F - F"
# angle = 180 / 2
# l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F + F - F - FFF + F + F - FF"))
# l_sys.generate_path(2)
# print(l_sys.state)
# l_sys.draw_turtle((0, 000), 0)
#
# 9. Снежинка
# f_len = 1
# axiom = "[ F ] + [ F ] + [ F ] + [ F ] + [ F ] + [ F ]"
# angle = 180 / 3
# l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F [ + + F ] [ - F F ] F F [ + F ] [ - F ] F F"))
# l_sys.generate_path(3)
# print(l_sys.state)
# l_sys.draw_turtle((0, -50), 0)

#
# 10. Снежинка Коха
# f_len = 10
# axiom = "F++F++F"
# angle = 60
# l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F-F++F-F"))
# l_sys.generate_path(3)
# print(l_sys.state)
# l_sys.draw_turtle((0, -50), 0)
#
# 11. Кривая Пеано
# axiom = "F"
# angle = 180 / 2
# l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F - F + F + F + F - F - F - F + F"))
# l_sys.generate_path(5)
# print(l_sys.state)
# l_sys.draw_turtle((0, -50), 0)
