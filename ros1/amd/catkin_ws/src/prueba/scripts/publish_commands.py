#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import time

def publish_commands():
    # Inicializar el nodo
    rospy.init_node('command_publisher', anonymous=True)

    # Crear los publishers para cada tópico
    nema_pub = rospy.Publisher('/hwd/nema_joint_controller/command', Float64, queue_size=10)
    right_arm_pub = rospy.Publisher('/hwd/right_arm_to_carriage_controller/command', Float64, queue_size=10)
    servo0_pub = rospy.Publisher('/hwd/manipulator/servo0/command', Float64, queue_size=10)
    servo1_pub = rospy.Publisher('/hwd/manipulator/servo1/command', Float64, queue_size=10)
    servo2_pub = rospy.Publisher('/hwd/manipulator/servo2/command', Float64, queue_size=10)
    servo3_pub = rospy.Publisher('/hwd/manipulator/servo3/command', Float64, queue_size=10)
    valve_pub = rospy.Publisher('/hwd/manipulator/valve/command', Float64, queue_size=10)

    # Esperar un poco para asegurar que los publishers se conecten
    rospy.sleep(2)

    # Publicar un valor de 5.0 en cada tópico con pausas entre ellos
    rate = rospy.Rate(0.5)  # Publica con una pausa de 2 segundos (0.5 Hz)

    for _ in range(5):
        nema_pub.publish(5.0)
        right_arm_pub.publish(5.0)
        servo0_pub.publish(5.0)
        servo1_pub.publish(5.0)
        servo2_pub.publish(5.0)
        servo3_pub.publish(5.0)
        valve_pub.publish(5.0)
        
        rospy.loginfo("Publicado valor 5.0 en todos los tópicos.")
        
        # Pausa de 2 segundos antes de la siguiente publicación
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_commands()
    except rospy.ROSInterruptException:
        pass
