from details_scrapper_app.models import Record


def start():
    # set this to where you want to get this mails
    email = "tarangranpara1998@gmail.com"

    # records
    # setting prices high so that functionality can be tested
    records = [
        {
            'link': 'https://www.amazon.in/Amazon-Brand-Solimo-Cotton-Paisley/dp/B06WLGNSVJ/ref=sr_1_4?dchild=1&pf_rd_p=767e7347-016c-46a6-99ec-68c52fb5983e&pf_rd_r=6NXTTVVVV37KZ1AA1NR3&qid=1610128104&refinements=p_n_format_browse-bin%3A19560802031&s=kitchen&sr=1-4',
            'site': 'a',
            'email': email,
            'price': 100000
        },

        {
            'link': 'https://www.flipkart.com/kraasa-young-choice-sneakers-men/p/itmf62b83d8d3843?pid=SHOFMHDJKUYDMSZU&lid=LSTSHOFMHDJKUYDMSZUDKD8BL&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_5_4.dealCard.OMU_8H304MD10EWH_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_5_NA_view-all_2&fm=neo%2Fmerchandising&iid=en_1VYC3NfozZHOwM0BxWgOIGuoArC0J3%2F9OHTNS8NrtGXDgwoIH8tzIJ3lYsTTAqN%2FtrqYEj%2F5PLc9beum%2FyrbYQ%3D%3D&ppt=browse&ppn=browse&ssid=tf852eo2e80000001610128149606',
            'site': 'f',
            'email': email,
            'price': 100000
        },

        {
            'link': 'https://www.snapdeal.com/product/activa-act32-smart-80-cm/662384079103#bcrumbLabelId:64',
            'site': 's',
            'email': email,
            'price': 1000000
        }
    ]

    for record in records:
        Record.objects.create(
            link=record.get('link'),
            site=record.get('site'),
            price=record.get('price'),
            email=record.get('email')
        )

        print(record)
        print('Record created.')
