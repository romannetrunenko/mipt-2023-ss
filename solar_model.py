# coding: utf-8
# license: GPLv3
gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""
physical_time = 0

def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += -gravitational_constant * body.m * obj.m / r**3 * (body.x - obj.x)
        body.Fy += -gravitational_constant * body.m * obj.m / r**3 * (body.y - obj.y)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.x += body.Vx * dt + ax * dt**2 / 2
    body.Vx += ax*dt

    ay = body.Fy / body.m
    body.y += body.Vy * dt + ay * dt ** 2 / 2
    body.Vy += ay * dt

time_since_last_stat_save = 0
stat_save_time_resolution = 300000

def update_stats(space_objects, dt):
    global time_since_last_stat_save
    time_since_last_stat_save += dt
    if time_since_last_stat_save > stat_save_time_resolution:
        time_since_last_stat_save = 0
        for obj in space_objects:
            obj.t_stats.append(physical_time)
            obj.x_stats.append(obj.x)
            obj.y_stats.append(obj.y)
            obj.vx_stats.append(obj.Vx)
            obj.vy_stats.append(obj.Vy)

def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.
    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)
    update_stats(space_objects, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
