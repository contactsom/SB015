print("START- This is Example for String formating using template strings")

simplilearnCareers="{} careers advanced"

careers=5000

print(simplilearnCareers.format(careers)) # 5000 careers advanced

print("---------------------------------------------------------------------------------------------------")

careerReport="{}% report career benefits including promotion or a new job"
reportPercent=85
print(careerReport.format(reportPercent))


print("---------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------")

simplilearnCisco='''{edtech} upskill {company} Employee with 
                    Worlds no {rank} {technology} {mode} Training in {country} 
                    provided {moneyback} % Money Back Gurienty and {supportHour} Support
                    '''
print(simplilearnCisco.format(
                                edtech="Simplilearn",
                                company="CISCO",
                                rank=1,
                                technology="Python",
                                mode="online",
                                country="INDIA",
                                moneyback=100,
                                supportHour="24X7"
                            ))














print("END- This is Example for String formating ")

