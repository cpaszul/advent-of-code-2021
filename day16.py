from math import prod

DEFAULT_INPUT = 'day16.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        h = f.readline()
    packet = bin(int(h, 16))[2:]
    if h[0] == '0':
        packet = '0000' + packet
    if h[1] == '1':
        packet = '000' + packet
    if h[0] in '23':
        packet = '00' + packet
    if h[0] in '4567':
        packet = '0' + packet
    return version_sum(packet, 0)[0]

def version_sum(packet: str, starting_index: int) -> tuple[int, int]:
    packet_version = int(packet[starting_index :starting_index + 3], 2)
    packet_type = int(packet[starting_index + 3:starting_index + 6], 2)
    if packet_type == 4:
        i = 0
        while packet[starting_index + 6 + i] == '1':
            i += 5
        return packet_version, starting_index + 11 + i
    else:
        length_type = packet[starting_index + 6]
        if length_type == '1':
            number_of_subpackets = int(packet[starting_index + 7:starting_index + 18], 2)
            current_index = starting_index + 18
            for _ in range(number_of_subpackets):
                subpacket_version_sum, new_index = version_sum(packet, current_index)
                packet_version += subpacket_version_sum
                current_index = new_index
        else:
            bit_length = int(packet[starting_index + 7:starting_index + 22], 2)
            current_index = starting_index + 22
            ending_index = starting_index + 22 + bit_length
            while current_index != ending_index:
                subpacket_version_sum, new_index = version_sum(packet, current_index)
                packet_version += subpacket_version_sum
                current_index = new_index
        return packet_version, current_index
            

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        h = f.readline()
    packet = bin(int(h, 16))[2:]
    if h[0] == '0':
        packet = '0000' + packet
    if h[1] == '1':
        packet = '000' + packet
    if h[0] in '23':
        packet = '00' + packet
    if h[0] in '4567':
        packet = '0' + packet
    return evaluate_packet(packet, 0)[0]

def evaluate_packet(packet: str, starting_index: int) -> tuple[int, int]:
    packet_type = int(packet[starting_index + 3:starting_index + 6], 2)
    if packet_type == 4:
        i = 0
        number = ''
        number_finished = False
        while not number_finished:
            if packet[starting_index + 6 + i] == '0':
                number_finished = True
            number += packet[starting_index + 7 + i:starting_index + 11 + i]
            i += 5
        return int(number, 2), starting_index + 6 + i
    else:
        length_type = packet[starting_index + 6]
        subpackets = []
        if length_type == '1':
            number_of_subpackets = int(packet[starting_index + 7:starting_index + 18], 2)
            current_index = starting_index + 18
            for _ in range(number_of_subpackets):
                subpacket_value, new_index = evaluate_packet(packet, current_index)
                subpackets.append(subpacket_value)
                current_index = new_index
        else:
            bit_length = int(packet[starting_index + 7:starting_index + 22], 2)
            current_index = starting_index + 22
            ending_index = starting_index + 22 + bit_length
            while current_index != ending_index:
                subpacket_value, new_index = evaluate_packet(packet, current_index)
                subpackets.append(subpacket_value)
                current_index = new_index
        ops = [sum, prod, min, max, None, lambda x, y: 1 if x > y else 0,
               lambda x, y: 1 if x < y else 0, lambda x, y: 1 if x == y else 0]
        if packet_type in (5, 6, 7):
            return ops[packet_type](*subpackets), current_index
        return ops[packet_type](subpackets), current_index

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
