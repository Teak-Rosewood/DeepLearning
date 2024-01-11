from degrees import degrees

class Graph:
    def __init__(self,node_list):
        self.graph_list = {}

        for node in node_list:
            self.graph_list[node] = []
        
    def add_adjacency(self,node1,node2):
        self.graph_list[node1].append(node2)

    def depth_first_search(self,start_key,required_key):
        stack = []
        stack.append((start_key,0))
        possible_answers = []

        while (len(stack)>0):
            current = stack.pop()
            current_node = current[0]
            current_depth = current[1]

            if current_node == required_key:
                possible_answers.append(current_depth)
                continue
            
            if current_depth >= 6:
                continue
            
            for adjacent in self.graph_list[current_node]:
                stack.append((adjacent,current_depth+1))

        try:
            return min(possible_answers)
        except:
            return 0

    def breadth_first_search(self,start_key,required_key):
        queue = []
        queue.append((start_key,0))
        possible_answers = []

        while (len(queue)>0):
            current = queue.pop(0)
            current_node = current[0]
            current_depth = current[1]

            if current_node == required_key:
                possible_answers.append(current_depth)
                continue
            
            if current_depth >= 6:
                continue
            
            for adjacent in self.graph_list[current_node]:
                queue.append((adjacent,current_depth+1))
        try:
            return min(possible_answers)
        except:
            return 0

def six_degrees_of_kevin_bacon(find_actor,graph,type=0):
    get_id = list(degrees.names[find_actor])[0]
    print(graph.depth_first_search('102',get_id))

degrees.load_data('degrees/small')

graph = Graph(list(degrees.people.keys()))

for star in degrees.people:
    movies = degrees.people[star]['movies']

    for movie in movies:
        co_stars = degrees.movies[movie]['stars']
        for co_star in co_stars:
            graph.add_adjacency(star,co_star)

six_degrees_of_kevin_bacon('Tom Cruise'.lower(),graph)






        


