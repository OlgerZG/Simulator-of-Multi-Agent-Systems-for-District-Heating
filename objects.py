class simulation():
    def __init__(self, name, global_time ,time_step):
        self.name = name
        self.global_time = global_time
        self.time_step   = time_step


class agent(): 
    def __init__(self, name,input,init_pressure):
        self.name = name 
        self.input = input # input = reference point (control term)
        self.links = []
        self.pressure = init_pressure # Pa

    def add_link(self, *agents):
        self.links.extend(agents)

    def get_connections_string(self):
        connection_string = f"{self.name} is linked to: "
        for agent in self.links:
            connection_string += f"{agent.name} "
        return connection_string
    
    def print_connections_string(self):
        print(self.get_connections_string())
