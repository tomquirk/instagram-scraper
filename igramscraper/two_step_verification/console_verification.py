from .two_step_verification_abstract_class import TwoStepVerificationAbstractClass


class ConsoleVerification(TwoStepVerificationAbstractClass):

    def get_verification_type(self, choices):
        if not isinstance(choices, list):
            if 'phone' in choices['label'].lower():
                phone_number = self.get_phone_number()
                return {
                    'phone_number': phone_number
                }
        elif len(choices) > 1:
            possible_values = {}
            print('Select where to send security code')
            for choice in choices:
                print(choice['label'] + ' - ' + str(choice['value']))
                possible_values[str(choice['value'])] = True

            selected_choice = None

            while (not selected_choice in possible_values.keys()):
                if (selected_choice):
                    print('Wrong choice. Try again')

                selected_choice = input('Your choice: ').strip()
        elif len(choices) == 1:
            print('Message with security code sent to: ' + choices[0]['label'])
            selected_choice = choices[0]['value']

        return {'choice': selected_choice}

    def get_security_code(self):
        """

        :return: string
        """
        security_code = ''
        while (len(security_code) != 6 and not security_code.isdigit()):
            if (security_code):
                print('Wrong security code')

            security_code = input('Enter security code: ').strip()

        return security_code

    def get_phone_number(self):
        phone_number = input('Enter phone number for SMS verification: ').strip()
        return phone_number
