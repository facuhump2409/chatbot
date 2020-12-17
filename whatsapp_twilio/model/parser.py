class Parser:
    def parse_message(msg):
        order_id_regex = "(?i)pedido: \K.+"
        products_regex = "— \K.+ (?=>)" #TODO manejar la cantidad
        total = "Total: \K.+"
        payment_method = "Forma de pago: \*\K.+(?= \*)"
        delivery = "(?i)Env.o : \*\K.+(?= \*)"
        nameAndSurname = "(?i)Nombre y apellido: \K.+"
        mail = "(?i)correo electr.nico : \K.+"
        address = "(?i)Domicilio .+: \K.+" #TODO ver de cambiar que en uno sea localidad y despues provincia




    def get_response(self,msg):
        order = self.parse_message(msg)