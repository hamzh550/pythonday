print ("Welcome to the tip calculator!?\n")
bill =float (input("what is the final bill?\n"))
howmanyppl=int(input("how may pepole to split the bill??\n"))
Tip_amout=float(input("how much you want add tip?\n"))
totalbillperperson=(bill + Tip_amout)/howmanyppl
final_amount=round(totalbillperperson,2)


print(f"final Bill is :${final_amount} " ) 
