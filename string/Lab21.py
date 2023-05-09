print("START- This is Example for String formating ")


simplilearnBootcamp="World’s 1 Online Bootcamp 85% report career benefits including promotion or a new job"
print(simplilearnBootcamp)

print("---------------------------------------------------------------------------------------------------")

print("World %(rank)d Online Bootcamp 85 report career benefits including promotion or a new job"
        %{
          'rank':1
         }
      )

print("World %(rank)d Online Bootcamp 85 report career benefits including promotion or a new job"
        %{
          'rank':2
         }
      )


print("******************************************************************************************************")

print(" %(edtech)s  is no %(rank)d %(course)s  course in %(country)s for a %(stream)s. "
      %{
        "edtech":"Simplilearn's",
        "rank":1,
        "course":"PMP training",
        "country":"INDIA",
        "stream" :"project management professional"
      })







print("END- This is Example for String formating ")