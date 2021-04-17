import pgzrun
import random  # ����������� ���������� ��������� �����  
alien = Actor('alien')  # �������� ������� �����
speed = random.randint(1, 3)  # ��������� ��������
WIDTH = 500  # ����� �������� ����
HEIGHT = 500  # ������ �������� ����
step = 10  # ���-�� ����� � ��������� �������
choose = 1  # ����� �����������
def draw():  # ������� ��������� ������ � �����
    screen.clear()  
    alien.draw()  
def update():  
    global step, choose  
    if step == 10:  # ��������� �����������
        choose = random.randint(1, 4)
        step = 0
    if choose == 1:  # ����������� 1 (������)
        alien.left += speed
    elif choose == 2:  # ����������� 2 (�����)
        alien.left -= speed
    elif choose == 3:  # ����������� 3 (�����)
        alien.top -= speed
    else:  # ����������� 4 (����)
        alien.top += speed    
    if alien.left > WIDTH - alien.width:  # ����������� �������� ������
        alien.left -= speed  
    elif alien.left < 0:  # ����������� �������� �����
        alien.left += speed
    elif alien.top < 0:  # ����������� �������� ������
        alien.top += speed 
    elif alien.top > HEIGHT - alien.height:  # ����������� �������� �����
        alien.top -= speed  
    step += 1  # ��������� ���
alien.center = 250, 250  # ��������� ���������
pgzrun.go()