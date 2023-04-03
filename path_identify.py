import send_serial as ss
import indicator_control as ind
import txt2voice as t2v

def path_switch(path):
    if(path=='/poweron'):
        print('try poweron')
        ss.poweron()
        print('poweron has finished!')

    if (path == '/poweroff'):
        print('try poweroff')
        ss.poweroff()
        print('poweroff has finished!')

    if (path == '/indicator_on'):
        print('try indicator_on')
        # t2v.speak_shdlh()
        ind.indicator_on()
        print('indicator_on has finished!')

    if (path == '/indicator_off'):
        print('try indicator_off')
        ind.indicator_off()
        print('indicator_off has finished!')

    if (path == '/12345'):
        print('try 12345-shdlh')
        t2v.speak_shdlh()
        print('12345-shdlh has finished!')