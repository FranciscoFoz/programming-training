import csv
from spaceship_titanic import SpaceshipTitanic

def csv_para_titanic_csv(caminho, encoding):
    
    linhas = []
    
    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)
        
        for linha in leitor:
            PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported = linha
            
            leitura = SpaceshipTitanic(PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported)  
            linhas.append(leitura)

    return linhas

class SpaceshipTitanic:
    
    def __init__(self,PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported):
        self.PassengerId = PassengerId
        self.HomePlanet = HomePlanet
        self.CryoSleep = CryoSleep
        self.Cabin = Cabin
        self.Destination = Destination
        self.Age = Age
        self.VIP = VIP
        self.RoomService = RoomService
        self.FoodCourt = FoodCourt
        self.ShoppingMall = ShoppingMall
        self.Spa = Spa
        self.VRDeck = VRDeck
        self.Name = Name 
        self.Transported = Transported

csv_para_titanic_csv('4 - Arquivos/Lendo_arquivos_IO/IO_csv/spaceship_titanic_train.csv',encoding='latin_1')
