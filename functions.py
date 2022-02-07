def axis_rotation(angle, axis):
    """
    Takes in an angle in degrees and a axis to rotate around and returns rotation matrix.

        Parameters:
                angle (float): Angle of rotation
                axis (str): Axis of rotation ('x','y', or 'z') 

        Returns:
                Rotation matrix of angle about axis of rotation entered
    """
    
    #convert angle from degrees to radians
    angle_rad = math.radians(angle)
    
    #Define s as sin(angle in radians)
    s = np.sin(angle_rad)
    #Define c as sin(angle in radians)
    c = np.cos(angle_rad)


    if axis == 'x':
        Rx = np.array([(1, 0, 0),
                       (0, c, -s),
                       (0, s, c)], dtype=float)
        return (Rx)
    elif axis == 'y':
        Ry = np.array([(c, 0, s),
                       (0, 1, 0),
                       (-s, 0, c)], dtype=float)
        return (Ry)
    elif axis == 'z':
        Rx = np.array([(c, -s, 0),
                       (s, c, 0),
                       (0, 0, 1)], dtype=float)
        return (Rx)
    else:
        print("Error")


def transform(angle, axis, pos):
    """
    Takes in an angle in degrees and rotation axis of the base frame or custom axis vector to rotate around
    and the subsequent 1x3 translation vector  and returns the transform rotation matrix.

        Parameters:
                angle (float): Angle of rotation
                axis (np.array or str): Custom Axis of rotation vector array ([0, 0, 0]) or str for axis of rotation ('x','y', or 'z')
                pos (np.array): Translation vector in a 1x3 matrix

        Returns:
                Rotation transform matrix of a angle about rotation axis of the base frame or custom axis vector of rotation by the custom translation vector entered
    """
    #Check if axis is a string
    if isstring(axis) == 1:
        #Check if axis is rotation about axis x, y, or z
        if axis == 'x' or axis == 'y' or axis == 'z':
            r_m = axis_rotation(angle, axis)
    elif axis.size == 3:
        r_m = custom_axis_rotation(angle, axis)
    
    t_v = pos

    transform_matrix = np.array([(r_m[0,0], r_m[0,1], r_m[0,2], t_v[0]),
                                 (r_m[1,0], r_m[1,1], r_m[1,2], t_v[1]),
                                 (r_m[2,0], r_m[2,1], r_m[2,2], t_v[2]),
                                 (0, 0, 0, 1)], dtype=float)
    return transform_matrix

