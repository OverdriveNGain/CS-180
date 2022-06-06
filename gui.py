from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

GENDERS = ["", "Male", "Female"]

inputAge = None

def callbackGenerateMeals():
    print(f"Generate meals! ({inputAge.get()}) ({inputGender.get()})")

def callbackPreviousMeals():
    print(f"Previous Meal!")

def callbackNextMeals():
    print(f"Next Meal!")

root = Tk()
# root.geometry('400x600')

# Frame : Logo
logoFrame = Frame(root)
logoImage = ImageTk.PhotoImage(Image.open("logo.png"))  
logoImageLabel = Label(logoFrame, image = logoImage)
logoImageLabel.pack()
logoFrame.grid(row=0, column=0)

# Frame : Input
frameInput = Frame(root)
Label(frameInput, text = "Age").grid(row=0,column=0)
inputAge=IntVar()
frameInputAgeEntry = Entry(frameInput, textvariable=inputAge, width=5)
frameInputAgeEntry.insert(0, "")
frameInputAgeEntry.grid(row=0,column=1)
Label(frameInput, text = "Gender").grid(row=0,column=2)
inputGender = StringVar()
inputGender.set(GENDERS[0])
op = OptionMenu(frameInput, inputGender, *GENDERS)
op.config(width=8)
op.grid(row=0,column=3)
Button(frameInput, text ="Generate Meals!", command = callbackGenerateMeals).grid(row=0,column=4)
frameInput.grid(row=1, column=0)

# Frame : Generated Meals
frameGenerateMeals = Frame(root)
Label(frameGenerateMeals, text = "GENERATED MEALS").grid(row=0, column=0)
frameMealsGrid = Frame(frameGenerateMeals)
def dishFrame(frameMealsGrid, row, column, dishName, scores, ingredients):
    dish1 = Frame(frameMealsGrid)
    dish1UpperPanel = Frame(dish1)
    Label(dish1UpperPanel, text = "Name").grid(row=0,column=0)
    Label(dish1UpperPanel, text = dishName).grid(row=0,column=1)
    Label(dish1UpperPanel, text = "Ingredients").grid(row=1,column=0)
    ingredientsFrame = Frame(dish1UpperPanel)
    scrollbar = Scrollbar(ingredientsFrame)
    scrollbar.pack(side = RIGHT, fill = BOTH)
    ingredientsListbox = Listbox(ingredientsFrame)
    ingredientsListbox.pack(side = LEFT, fill = BOTH)
    for ingredient in ingredients:
        ingredientsListbox.insert(END, ingredient)
    ingredientsListbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = ingredientsListbox.yview)
    ingredientsFrame.grid(row=1,column=1)
    dish1UpperPanel.grid(row=0, column=0)
    dish1LowerPanel = Frame(dish1)
    Label(dish1LowerPanel, text = "CALORIES").grid(row=0,column=0)
    Label(dish1LowerPanel, text = "PROTEIN").grid(row=0,column=1)
    Label(dish1LowerPanel, text = "FAT").grid(row=0,column=2)
    Label(dish1LowerPanel, text = "SODIUM").grid(row=0,column=3)
    Label(dish1LowerPanel, text = "RATING").grid(row=0,column=4)
    Label(dish1LowerPanel, text = str(scores[0])).grid(row=1,column=0)
    Label(dish1LowerPanel, text = str(scores[1])).grid(row=1,column=1)
    Label(dish1LowerPanel, text = str(scores[2])).grid(row=1,column=2)
    Label(dish1LowerPanel, text = str(scores[3])).grid(row=1,column=3)
    Label(dish1LowerPanel, text = str(scores[4])).grid(row=1,column=4)
    dish1LowerPanel.grid(row=1, column=0)
    dish1.grid(row=row, column=column)
dishFrame(frameMealsGrid, 0, 0, "Tuna Ala Mode", [240, 220, 100, 150, 50], ["Egg", "Milk","Flower", "Soil", "Trash"])
dishFrame(frameMealsGrid, 0, 1, "Sunny Side Up", [100, 200, 3, 4, 50], ["Egg", "Milk","Flower", "Soil", "Trash"])
dishFrame(frameMealsGrid, 1, 0, "Crabs", [1, 2, 3, 4, 5], ["Egg", "Milk","Flower", "Soil", "Trash"])
frameMealsGrid.grid(row=1, column=0)
Label(frameGenerateMeals, text = "TOTAL RATING: 69").grid(row=2, column=0)
frameGenerateMeals.grid(row=2, column=0)

# Frame : Lower Input
frameLowerInput = Frame(root)
Button(frameLowerInput, text ="Previous Meal", command = callbackPreviousMeals).grid(row=0,column=0)
Button(frameLowerInput, text ="Next Meal", command = callbackNextMeals).grid(row=0,column=1)
frameLowerInput.grid(row=3, column=0)

root.mainloop()