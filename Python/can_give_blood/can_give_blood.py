#----------------------------------------------------------------#
def can_give_blood(donor, receiver):
	donor_blood = "".join(i for i in donor if i.isalpha())
	receiver_blood = "".join(i for i in receiver if i.isalpha())
	
	doner_rh = "".join(i for i in donor 
		if i not in donor_blood)
	receiver_rh = "".join(i for i in receiver
	 if i not in receiver_blood)

	if donor == "O-":
		return True

	if donor == "O+":
		return receiver_rh == "+"

	return donor_blood in receiver_blood
#----------------------------------------------------------------#