tasks = {
    "planimetria": [
        ['(Задание 1) Площадь треугольника ABC равна 176, DE — средняя линия. Найдите площадь треугольника CDE', 44, 'test.svg', r'''
        Так как CM— медиана, то AM=MC (свойство медианы в прямоугольном треугольнике), а значит, углы A и ACM равны как углы при основании равнобедренного треугольника.\(\scriptsize
                            \angle M C D = \angle C - \frac{\angle C}{2} - \angle A C M
                            = \frac{\angle C}{2} - \angle A
                            = \frac{\angle C}{2} - (90^{\circ} - \angle B)
                            = 45^{\circ} - 24^{\circ} = 21^{\circ}
                            \). Ответ: 21.''', '1. Планиметрия']
    ],
    'vectors': [
        ['Две стороны прямоугольника ABCD равны 6 и 8. Найдите длину суммы векторов AB и AD', 10, '', 'Сумма векторов AB и AD равна вектору AC Вектор AC образует в прямоугольнике два прямоугольных треугольника. Поэтому по теореме Пифагора \(\scriptsize AC = \sqrt{6^2 + 8^2} = 10\)', '2. Векторы']
    ],
    'stereometry': [
        ['Площадь основания конуса равна 45. Плоскость, параллельная плоскости основания конуса, делит его высоту на отрезки длиной 4 и 8, считая от вершины. Найдите площадь сечения конуса этой плоскостью.', 5, '3_1.svg', 'Исходный и отсеченный конус подобны с коэффициентом подобия 3. Площади поверхностей подобных тел относятся как квадрат коэффициента подобия. Поэтому площадь основания отсечённого конуса в 9 раз меньше площади основания исходного. Тем самым, она равна 5.', '3. Стереометрия'],
        ['Объём куба равен 24. Найдите объём треугольной призмы, отсекаемой от куба плоскостью, проходящей через середины двух рёбер, выходящих из одной вершины, и параллельной третьему ребру, выходящему из этой же вершины.', 3, '3_2.svg', 'Поскольку высота куба равна высоте призмы, их объемы пропорциональны площадям их оснований. Площадь основания построенной призмы в 8 раз меньше площади основания исходной, поэтому искомый объем призмы равен 24:8=3.', '3. Стереометрия'],
        ['Площадь основания конуса равна 9. Плоскость, параллельная плоскости основания конуса, делит его высоту на отрезки длиной 3 и 6, считая от вершины. Найдите площадь сечения конуса этой плоскостью.', '1', '3_3.svg', 'Сечение плоскостью, параллельной основанию, представляет собой круг, радиус которого относится к радиусу основания конуса как 3:9. Площади подобных фигур относятся как квадрат коэффициента подобия, поэтому площадь сечения в 9 раз меньше площади основания. Тем самым, она равна 1.', '3. Стереометрия'],
        ['Найдите объём правильной шестиугольной пирамиды SABCDEF, если объём треугольной пирамиды SABC равен 33.', '198', '3_4.svg', 'Данные пирамиды имеют общую высоту, поэтому их объемы относятся как площади их оснований. Площадь правильного шестиугольника ABCDEF в 6 раз больше площади треугольника АВС. Поэтому объем шестиугольной пирамиды SABCDEF в 6 раз больше объема пирамиды SABC, он равен 33·6 = 198', '3. Стереометрия'],
        ['Площадь полной поверхности конуса равна 164. Параллельно основанию конуса проведено сечение, делящее высоту в отношении 1:1, считая от вершины конуса. Найдите площадь полной поверхности отсечённого конуса.', '41', '3_5.svg', 'Исходный и отсеченный конус подобны с коэффициентом подобия 2. Площади поверхностей подобных тел относятся как квадрат коэффициента подобия. Поэтому площадь отсеченного конуса в 4 раза меньше площади поверхности исходного. Тем самым, она равна 41.', '3. Стереометрия']
    ],
    'probability_beginnings': [
        ['В случайном эксперименте бросают две игральные кости. Найдите вероятность того, что в сумме выпадет 10 очков. Результат округлите до сотых.', '0.08', '', 'Количество исходов, при которых в результате броска игральных костей выпадет 10 очков, равно 3: 4+6, 5+5, 6+4. Каждый из кубиков может выпасть шестью вариантами, поэтому общее число исходов равно 6·6=36. Следовательно, вероятность того, что в сумме выпадет 10 очков, равна 3/36 = 0.083', '4. Начала теории вероятностей'],
        ['За круглый стол на 17 стульев в случайном порядке рассаживаются 15 мальчиков и 2 девочки. Найдите вероятность того, что девочки будут сидеть рядом.', '0.125', '', 'Пусть первой за стол сядет девочка, тогда рядом с ней есть два места, на каждое из которых претендует 16 человека, из которых только одна девочка. Таким образом, вероятность, что девочки будут сидеть рядом равна 2 · 1/16 = 0.125', '4. Начала теории вероятностей'],
        ['В случайном эксперименте симметричную монету бросают трижды. Найдите вероятность того, что наступит исход ООР (в первый и второй разы выпадает орёл, в третий — решка).', '0.125', '', 'Всего возможных исходов  — восемь: ООО, ООР, ОРО, ОРР, РРР, РРО, РОО, РОР. Благоприятным является один: орел-орел-решка. Следовательно, искомая вероятность равна 1 : 8 = 0,125.', '4. Начала теории вероятностей']
    ],
    'complex_events_probability': [
        ['В ящике семь красных и три синих фломастера. Фломастеры вытаскивают по очереди в случайном порядке. Какова вероятность того, что первый раз синий фломастер появится третьим по счету?', '0.175', '', 'Изобразим с помощью дерева возможные исходы. Последовательность исходов, приводящая к событию «первый раз синий фломастер появится третьим по счету» выделена оранжевым цветом. Искомая вероятность равна 7/10 · 6/9 · 3/8 - 7/40 = 0.175', '5. Вероятности сложных событий']
    ],
    'simple_equations': [
        ['Найдите корень уравнения', '2', '6_1.svg', r'Используем формулу \(\scriptsize\log_x d^n = \frac{n}{n}\)  \(\scriptsize\log_8 2^{8x-4} = 4 \Leftrightarrow \log_{7^3} 2^{kx-4} = 4 \Leftrightarrow \frac{8x-4}{3} = 4 \Leftrightarrow 8x-4 = 12 \Leftrightarrow x=2\)', '6. Простейшие уравнения'],
        ['Найдите корень уравнения', '321', '6_2.svg', r'Возведем в квадрат: \(\scriptsize\sqrt{\frac{6}{2x-42}} = \frac{1}{10} \Leftrightarrow \frac{6}{2x-42} = \frac{1}{100} \Leftrightarrow 600 = 2x-42 \Leftrightarrow x = 321\)', '6. Простейшие уравнения']
    ],
    'calculations_transformations': [
        ['Найдите значение выражения', 1, '7_1.svg', r'\(\scriptsize\frac{\sqrt[4]{3} \cdot \sqrt[16]{3}}{\sqrt[16]{3}} = \frac{3+5 \cdot 3 \frac{1}{6}}{3^{\frac{1}{12}}} = 3^{\frac{1}{48}} + \frac{1}{16} - \frac{1}{12} = 3^0 = 1\)', '7. Вычисления и преобразования']
    ],
    'derivative_integral': [
        ['На рисунке изображён график функции y=f(x), определённой на интервале (-3; 10) Найдите количество точек, в которых производная функции f(x) равна 0.', 10, '8_1.svg', 'Производная изображенной на рисунке функции f(x) равна нулю в точках экстремумов: −2; −1; 0; 1; 2; 3; 6; 7; 8 и 9,6. Производная равна нулю в 10 точках.', '8.Производная и первообразная'],
        ['На рисунке изображен график функции y=f(x). Прямая, проходящая через начало координат, касается графика этой функции в точке с абсциссой 10. Найдите f`(10)', '-0.6', '8_2.svg', 'Значение производной в точке касания равно угловому коэффициенту касательной. Поскольку касательная проходит через начало координат, ее уравнение имеет вид y=kx Прямая проходит через точку (10;−6), значит, k=-0.6 Поскольку угловой коэффициент равен значению производной в точке касания получаем: f`(10)=-0.6', '8.Производная и первообразная']
    ],
    'applied_problems': [
        ['Некоторая компания продает свою продукцию по цене руб. за единицу, переменные затраты на производство одной единицы продукции составляют v=400 руб., постоянные расходы предприятия f = 6000000руб. в месяц. Месячная операционная прибыль предприятия (в рублях) вычисляется по формуле π(q) = q(p - v) - f Определите месячный объeм производства q (единиц продукции), при котором месячная операционная прибыль предприятия будет равна 500000руб.', 5500, '', 'Задача сводится к нахождению решения уравнения π(q) = 500000 руб. при заданных значениях цены за единицу p = 600 руб., переменных затрат на производство одной единицы продукции v = 400 руб. и постоянных расходов предприятия f = 6000000 руб. в месяц: \(\scriptsize\pi(q) = 500000 \Leftrightarrow q(p - v) - f_0 = 500000\) \(\scriptsize\Leftrightarrow q(600-400)-600000=500000 \Leftrightarrow q=5500\)', '9. Задачи с прикладным содержанием']
    ],
    'word_problems': [
        ['Баржа в 10:00 вышла изпункта А в пункт В, расположенный в 30км от А. Пробыв в пункте В 1 час 40 минут, баржа отправилась назад и вернулась в пункт А в 21:00 того же дня. Определите (в км/час) скорость течения реки, если известно, что собственная скорость баржи равна 7км/ч.', 2, '', r'Пусть u км/ч — скорость течения реки, тогда скорость баржи по течению равна  км/ч, а скорость баржи против течения равна  км/ч. Баржа вернулась в пункт A через 11 часов, но пробыла в пункте B  час 40 минут, поэтому общее время движения баржи дается уравнением: \(\scriptsize\frac{30}{7-u} + \frac{30}{7+u} = 11 - \frac{5}{3} \Leftrightarrow \frac{30 \cdot (7+u) + 30 \cdot (7-u)}{49-u^2} = \frac{28}{3} \Leftrightarrow \frac{30 \cdot 7 \cdot 2}{49-u^2} = \frac{28}{3} \Leftrightarrow\) \(\scriptsize 0 \Leftrightarrow \frac{1}{0} 90 = 2\left(49-\kappa^2\right) \Leftrightarrow u^2=4 \Leftrightarrow\left[\begin{array}{l}   u=2 ; \\   u=-2 \Leftrightarrow 0\end{array} \Leftrightarrow=2\right.\)', '10. Текстовые задачи'],
        ['Имеется два сплава. Первый содержит 10% никеля, второй — 35% никеля. Из этих двух сплавов получили третий сплав массой 175кг, содержащий 25% никеля. На сколько килограммов масса первого сплава была меньше массы второго?', '35', '', r'Пусть масса первого сплава m кг, а масса второго — (175 - m) кг. Тогда массовое содержание никеля в первом и втором сплавах 0.1m и 0.35(175 - m) соответственно. Из этих двух сплавов получили третий сплав массой 175кг, содержащий 25% никеля. Получаем уравнение: \(\scriptsize 0.1m + 0.35(175 - m) = 0.25 \cdot 175 \Leftrightarrow 0.1m - 0.35m + 0.35 \cdot 175 = 0.25 \cdot 175\) \(\scriptsize\Leftrightarrow 0.35 \cdot 175 - 0.25 \cdot 175 = 0.35m - 0.1 \, \mathrm{m} \Leftrightarrow 17.5 = 0.25m \Leftrightarrow m = 70\)', '10. Текстовые задачи']
    ],
    'function_graphs': [
        ['На рисунке изображён график функции f(x) = ax^2 + bx + c Найдите f(2)', -33, '11_1.svg', r'Из рисунка видно, что f(-5)=2, f(-4)=3 и f(-2)=1. Получаем систему уравнений, которую можно решить методом подстановки: \(\scriptsize\left\{\begin{array}{l}  25a - 5b + c = 2, \\  16a - 4b + c = 3, \\  4a - 2b + c = -1\end{array}\right.\Leftrightarrow\left\{\begin{array}{l}  25a - 5b + (2b - 4a - 1) = 2 \\  16a - 4b + (2b - 4a - 1) = 3 \\  c = 2b - 4a - 1\end{array}\right.\) \(\scriptsize\Leftrightarrow\left\{  \begin{array}{l}    7a - b = 1, \\    6a - b = 2, \\    c = 2b - 4a - 1  \end{array}\right.\Leftrightarrow\left\{  \begin{array}{l}    7a - (6a - 2) = 1, \\    b = 6a - 2, \\    c = 2b - 4a - 1  \end{array}\right.\Leftrightarrow\left\{  \begin{array}{l}    a = -1, \\    b = -8, \\    c = -13  \end{array}\right.\) \(\scriptsize f(2) = -2^2 - 8 \cdot 2 - 13 = -4 - 16 - 13 = -33\)', '11. Графики функций'],
        ['На рисунке изображён график функции', '-2', '11_2.svg', r'По графику f(0) = 0.5, тогда \(\scriptsize a \cdot \sin 0 + b = 0,5 \Leftrightarrow a \cdot 0 + b = 0,5 \Leftrightarrow b = 0,5\)', '11. Графики функций']
    ],
    'extrema_functions': [
        ['Найдите наибольшее значение функции y=57tgx - 57x + 23 на отрезке [-π/4; 0]', 23, '', r'Найдем производную заданной функции: \(\scriptsize y = 57 + \frac{1}{\cos^2 x} - 57 = 57\left(\frac{1}{\cos^2 x} - 1\right) = 57 \tan^2 x\). Найденная производная неотрицательна на заданном отрезке, заданная функция возрастает на нем, поэтому наибольшим значением функции на отрезке является \(\scriptsize y(0) = 57 \cdot \tan(0) - 57 \cdot 0 + 23 = 23\)', '12. Наибольшее и наименьшее значение функций']
    ]
}

themes = list(tasks.keys())