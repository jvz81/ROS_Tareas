#!/usr/bin/env python3

#Suscriptor que lee desde el publicador de nombre random_float
#y publicador de random_float_square
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('Cod2_E2_float', anonymous=True)	

float_value=0

#funcion para recibir el mensaje 
def callback(data):	
    global float_value
    float_value=data.data
    #print(float_value)
    #rospy.loginfo("I heard %f", float_value)

# se suscribe al topico
sub = rospy.Subscriber("random_float", Float64, callback)
# el codigo Cod1_float.py publica al topico 'random_float'

pub = rospy.Publisher('random_float_square', Float64, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor = round(float_value*float_value,2)
    print(valor)
    pub.publish(valor)
    rate.sleep() # delay de 1 segundo