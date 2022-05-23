def save_applicant_data(source, output):
    with open(output, 'w') as fl:
        for i in source:
            fl.write(f"{i['name']},{i['specialty']},{i['math']},{i['lang']},{i['eng']}\n")