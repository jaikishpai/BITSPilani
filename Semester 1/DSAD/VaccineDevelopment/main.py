# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Class representation for Immunization
class IMMUNIZATION:

    # constructor
    def __init__(self):
        self.vaccine_list = []
        self.edges_list = []
        self.queue = []

    def readInputfile(self, inputfile):
        read_data = open(inputfile, "r")  # opens the file in read mode
        #for line in read_data:
        #    self.vaccine_list.append(line.rstrip().split('/'))
        self.vaccine_list = [(line.strip()).split('/') for line in read_data]
        read_data.close()
        print(self.vaccine_list)

    def defineEdges(self, edges_list, node):
        self.edges_list.append(node)
        self.queue.append(node)
        while self.queue:
            s = self.queue.pop(0)
            print(s, end=" ")
            for neighbour in self.vaccine_list[s]:
                if neighbour not in self.edges_list:
                    self.edges_list.append(neighbour)
                    self.queue.append(neighbour)

    def displayAll(self):
        length = len(self.vaccine_list)
        vaccine_names = []
        strain_names = []
        for i in range(length):
            l = len(self.vaccine_list[i])
            j=0
            for j in range(l):
                if self.vaccine_list[i][0] in strain_names:
                    continue
                else:
                   strain_names.append(self.vaccine_list[i][0])
        count_of_strains = len(strain_names)
        print('Count of Strains:', count_of_strains)
        print('Strain Names:', strain_names)
        for i in range(length):
            l = len(self.vaccine_list[i])
            for j in range(1 , l):
                if self.vaccine_list[i][j] in vaccine_names:
                    continue
                else:
                   vaccine_names.append(self.vaccine_list[i][j])
        count_of_vaccines = len(vaccine_names)
        print('Count Vaccine', count_of_vaccines)
        print('Vaccine Names', vaccine_names)

    def displayStrains(self, vaccine):
        length = len(self.vaccine_list)
        find_strain_result = []
        for i in range(length):
            l = len(self.vaccine_list[i])
            for j in range(l):
                if vaccine in self.vaccine_list[i][j]:
                    find_strain_result.append(self.vaccine_list[i][0])
        if not find_strain_result:
            print("No virus strain found for the vaccine", vaccine)
        else:
            print('List of strain for vaccine', vaccine, ": ",  find_strain_result)

    def displayVaccine(self, strain):
        length = len(self.vaccine_list)
        find_vaccine_result = []
        for i in range(length):
            l = len(self.vaccine_list[i])
            for j in range(l):
                if strain in self.vaccine_list[i][0]:
                    for k in range (1,l):
                        if self.vaccine_list[i][k] in find_vaccine_result:
                            continue
                        else:
                            find_vaccine_result.append(self.vaccine_list[i][k])
        print('Vaccines for Strain ', strain, ': ', find_vaccine_result)










assignment = IMMUNIZATION()
assignment.readInputfile("inputfile.txt")
#print('length',len(assignment.vaccine_list[1]))
assignment.displayAll()
assignment.displayStrains('V4')
assignment.displayVaccine('S3')


#assignment.defineEdges(assignment.edges_list, "V1")

#print(len(assignment.vaccine_list))


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm
