# Project: Mirror Room

Модель оптических экспериментов в зеркальной комнате
Зеркальная комната представляет в плане произвольный замкнутый Мугольник (4≤ М≤ 9), каждая стена – плоское или сферическое зеркало. Для
проведения экспериментов необходимо определить для каждой стены комнаты
вид зеркала (плоское или сферическое), а для каждого сферического зеркала –
его тип (вогнутое или выпуклое) и радиус кривизны.
Основная функция программной системы – проведение оптического эксперимента, 
при котором из некоторой точки на одной из стен комнаты, 
под определенным углом к этой стене (угол может варьироваться от 0 до 180 градусов) выпускается луч света, 
и затем показывается его путь внутри комнаты с учетом отражений от зеркал. 
Траектория луча определяется физическими законами отражения от зеркальных поверхностей.
Цель моделирования – подбор пользователем системы параметров зеркал и исходного угла выпущенного луча, при которых луч, отражаясь от зеркальных стен, попадает в нужную точку (зону) комнаты.
При визуализации оптического эксперимента должен быть показан план комнаты и изображен путь луча в комнате.

Пользователь системы должен иметь возможность:
• определять число М стен комнаты и рисовать ее план (например, указывая мышью на экране компьютера угловые точки комнаты);
• задавать и изменять параметры зеркал (вид, тип, радиус кривизны), точку выпускания луча и его исходный угол;
• запоминать в файле копию оптического эксперимента, сохраняя все его параметры, и считывать сохраненную копию из файла в рабочее окно.
Требуется, чтобы указанные действия пользователь мог производить в произвольном, удобном для него порядке, и изменение одного параметра
эксперимента не должно затрагивать другие установленные параметры. Возможно усложнение рассматриваемой задачи, когда при отражении от
зеркальной поверхности учитывается эффект рассеивания света – в этом случае после нескольких отражений луч становится невидимым. При этом в число параметров эксперимента входят коэффициенты рассеивания каждого зеркала.
