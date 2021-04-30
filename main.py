import math
# Input Parameters
m = 100     # total weight (kg)
deg = 8     # max incline angle (degrees)
N = 2       # number of drive wheels
r = 0.08225 # wheel radius (m)
vel = 2.2   # Velocity (m/s)
accel = 0.4 # acceleration (m/s^2)
V = 24      # input voltage
level_time = 40 # 평지이동 시간 (분)
incline_time = 20 #오르막 이동 시간 (분)

Optime = level_time + incline_time # operating time (min)


effBATtoESC = 0.95
effESCtoMOT = 0.96
effMOT = 0.92
effTOT = effBATtoESC*effESCtoMOT*effMOT
rad = deg*math.pi/180
g = 9.81    # gravitational acceleration (m/s^2)
angvel = vel/r  #angular velocity of wheel (rad/s)

T1 = (1/effTOT)*(accel+g*math.sin(rad))*m*r/N   #오르막 이동
P1 = T1*angvel
I1 = P1/V

T2 = (1/effTOT)*accel*m*r/N   #평지이동
P2 = T2*angvel
I2 = P2/V

c = (I1*incline_time+I2*level_time)/60
rpm = angvel*60/(2*math.pi)

print("Max Power per motor: "+ str(round(P1,2))+" W")
print("Max Torque per motor: "+ str(round(T1,2))+" Nm")
print("Max Current per motor: "+str(round(I1,2))+" A")
print("Max RPM: "+ str(round(rpm,2))+" rpm")
print("Total Battery Capacity: "+str(round(c*2,2))+" Ah")
print("Total Operating Time: "+str(Optime)+" minutes")