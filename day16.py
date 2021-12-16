DEFAULT_INPUT = 'day16.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        h = f.readline()
    packet = bin(int(h, 16))[2:]
    if h[0] in '0123':
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
            return packet_version, current_index
        else:
            bit_length = int(packet[starting_index + 7:starting_index + 22], 2)
            current_index = starting_index + 22
            ending_index = starting_index + 22 + bit_length
            while current_index != ending_index:
                subpacket_version_sum, new_index = version_sum(packet, current_index)
                packet_version += subpacket_version_sum
                current_index = new_index
            return packet_version, current_index
            

def part_2(loc: str = DEFAULT_INPUT):
    with open(loc) as f:
        pass
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
