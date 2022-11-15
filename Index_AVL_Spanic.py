
class ChannelIndex:

    text = open("003_B1_SN2c2_FL_3500rpm_fl2.txt", "r")
    text = ' '.join(text)
    text = text.replace(",", " ").replace("&", ",").replace("\n", "").replace("[", "").replace("]", "")

    input_text = text.split("UNIT")[0]
    channel_ = input_text.split("=")[1]
    channel_list = channel_.split(",")

    flow_mass_index = int()
    crank_angle_index = int()

    for i in range(len(channel_list)):
        if channel_list[i] == " 'Crank Angle' ":
            crank_angle_index = i
            break

    for i in range(len(channel_list)):
        if channel_list[i] == "  ':flow:total_mass' ":
            flow_mass_index = i
            break












