import send_serial as ss
import indicator_control as ind

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
        ind.indicator_on()
        print('indicator_on has finished!')

    if (path == '/indicator_off'):
        print('try indicator_off')
        ind.indicator_off()
        print('indicator_off has finished!')