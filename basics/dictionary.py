if __name__ == '__main__':
    a_dict = {
        'first_name': 'Sophia',
        'last_name': 'Kalaskova',
        'prefix': 'Ms',
        'Birthday': '8th April, 1995',
        'Address': [
            {'id': '234234', 'locality': 'Posh'},
            {'id': '1234', 'country': 'Belarus'},
            {'id': '3453454', 'pincode': '34003'},
        ],
    }

    for key in a_dict:
        print('11111', key)
    for key, value in a_dict.items():
        print('22222', key, value, '<<<<<')
    print('33333', a_dict.get('Address'))

    for i in a_dict.get('Address'):
        print(';;;', i.get('id'), i)
        print('==', a_dict.get('Address').index(i))
        index = a_dict.get('Address').index(i)
        a_dict.get('Address')[0] = i + {'country': 'abbbccc'}
        # if i.get('id') == '1234':

        # users_results = data.get('results')
        # PMS_user_property_id = None
        # for i in users_results:
        #     local_user_modified_date = users_results.get('modified')
        #     local_user_property_id = users_results.get('property_id')
        #
        #     for j in PMS_users_results:
        #         if PMS_users_results.get('property_id') == local_user_property_id:
        #             PMS_user_property_id = PMS_users_results.get('property_id')
        #             PMS_user_modified_date = PMS_user_results.get('modified')

        #     if PMS_user_property_id != None:
        # if (local_user_property_id == PMS_user_property_id) and (local_user_modified_date  < PMS_user_modified_date):
        #              users_results, results[i] = [*PMS_user_data[i]]
