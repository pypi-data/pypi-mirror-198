def doppler_effect(frequency, observer_velocity, source_velocity, speed_of_sound=343.2):
    """
    Fungsi ini menghitung pergeseran frekuensi yang disebabkan oleh efek Doppler.
    
    Arguments:
        frequency (float): frekuensi asli dari gelombang suara, dalam Hz
        observer_velocity (float): kecepatan sumber, dalam m/s
        speed_of_sound (float): kecepatan suara, dalam m/s
        
    Returns:
        float: frekuensi yang bergeser, dalam Hz
    """
    vo = float(observer_velocity)
    vs = float(source_velocity)
    c = float(speed_of_sound)
    f = float(frequency)
    
    shifted_frequency = f * ((c + vo) / (c - vs))
    
    return shifted_frequency

def internal_energy(n, T, V, cv):
    """
    Menghitung energi dalam gas ideal menggunakan hukum gas ideal dan kapasitas panas spesifik.

    Arguuments:
    n (float): Jumlah mol gas.
    T (float): Suhu dalam Kelvin.
    V (float): Volume dalam m^3.
    cv (float): Kapasitas panas spesifik pada volume konstan dalam J/(mol*K).

    Returns:
    float: Energi dalam dalam Joule.
    """
    R = 8.314 # gas constant in J/(mol*K)
    U = n * cv * T + n * R * T * math.log(V)
    return U

def inersia_bola(m, r, pejal=False):
    """
    Fungsi ini menghitung momen inersia dari bola jika berputar terhadap pusat massanya. Mengukur kelembaman, atau seberapa susah benda tersebut berputar. 
    
    Arguments:
    m -- massa bola (kg) 
    r -- jari-jari bola (meter) 
    pejal -- apakah bola tersebut pejal? (True, False) 
    
    Returns:
    mi -- momen inersia (kg.m^2)
    """ 
    k = 2/3
    if pejal:
	k = 2/5
    mi = k*m*r**2
    return mi
