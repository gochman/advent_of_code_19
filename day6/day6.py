from collections import defaultdict

class Connection:
    def __init__(self, center, orbiter):
        self._center = center
        self._orbiter = orbiter

    def get_center(self):
        return self._center

    def get_orbiter(self):
        return self._orbiter


class Parser:
    def __init__(self):
        self._raw_connections = []
        with open(r"C:\Yoav's Disk\AdventOfCode\2019\day6\input.txt") as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        for line in content:
            self._raw_connections.append(line.split(")"))

    def generate_connections(self):
        # generate connections
        connections = []
        for line in self._raw_connections:
            connections.append(Connection(line[0],line[1]))

        return connections


class ProgramEngine:
    def __init__(self):

        self._orbit_center_map = defaultdict(str)  # Who do i circle?
        self._orbits_counter_map = {}
        my_parser = Parser()
        self._connections = my_parser.generate_connections()

    # def previous_execute(self):
    #     # Create center map
    #     for conn in self._connections:
    #         self._orbit_center_map[conn.get_orbiter()] = conn.get_center()
    #
    #     # Create orbits counter map
    #     for orbit in self._orbit_center_map:
    #         self._orbits_counter_map[orbit] = self.count_distance_to_father(orbit,"COM")
    #
    #     result = sum(self._orbits_counter_map.values())
    #     print("Total direct and indirect orbits: ", result)

    def find_first_common(self, list1, list2):
        for item in list1:  # assuming list1 is sorted
            if item in list2:
                return item

    def execute(self):
        # Create center map
        for conn in self._connections:
            self._orbit_center_map[conn.get_orbiter()] = conn.get_center()

        # Step 1: create routs of fathers for YOU ans SAN
        you_to_com_route = []
        self.generate_route("COM", "YOU", you_to_com_route)

        san_to_com_route = []
        self.generate_route("COM", "SAN", san_to_com_route)

        # Step 2: find first common father
        first_common_father = self.find_first_common(you_to_com_route,san_to_com_route)

        # step 3: calc dist YOU to FCF:
        dist_you_fcf = self.count_distance_to_father(first_common_father, "YOU")
        dist_san_fcf = self.count_distance_to_father(first_common_father, "SAN")

        # Step 4: print result
        print("Result is: ", dist_san_fcf + dist_you_fcf - 2)


    def generate_route(self, father, son, route):
        """
        Assuming we know they are related
        :return: a list of the route
        """
        if father == son:
            route.append(son)
        else:
            route.append(son)
            self.generate_route(father, self._orbit_center_map[son], route)

    def count_distance_to_father(self, father_name, son_name):
        if son_name == father_name:
            return 0
        else:
            return self.count_distance_to_father(father_name, self._orbit_center_map[son_name]) + 1

def main():
    my_engine = ProgramEngine()
    my_engine.execute()


if __name__ == "__main__":
    main()
