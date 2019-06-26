# Python: модуль timeit

Модуль определяет следующий класс:

#### class timeit.Timer([stmt='pass'[, setup='pass'[, timer=]]])
Класс для измерения скорости выполнения маленьких фрагментов кода. 

Конструктор принимает аргумент stmt содержащий выражение которое будет замерено, дополнительный аргумент setup представляющий собой выражение, выполняемое перед основным выражением. Функция таймера timer является платформозависимой (см. модуль doc string). Выражения могут содержать символы новой строки, если они не содержат многострочных строковых литералов. 

Для измерения времени выполнения первого выражения необходимо использовать метод timeit(). Метод repeat() удобен для многократного вызова timeit(), возвращает список с результатами. 

Новое в версии 2.6 

Параметры stmt и setup могут принимать объекты которые вызываются без аргументов.Это позволит встраивать вызовы в функцию таймер, который будет выполнен по timeit(). Обратите внимание, в этом случае будут произведены дополнительные затраты, из-за вызывов дополнительных функций.
Timer.print_exc([file=None])

Выводит информацию о полученном исключении из выполняемого кода. Приемущество данного метода перед стандартным выводом исключения состоит в том, что будут отображены исходные строки из компилированного шаблона. Дополнительный аргумент file указывает куда направить вывод об исключении, по-умолчанию это стандартный поток ошибок sys.stderr. 

Например так выглядит обычное сообщение об ошибке:

    import timeit, traceback 
    setup='a=5' 
    stmt='b=a/0' 
    t=timeit.Timer(stmt, setup) 
    try: 
        t.timeit() 
    except: 
       traceback.print_exc()

Результат:

    Traceback (most recent call last): 
        File "C:\Documents and Settings\User\tmp.py", line 43, in 
            t.timeit() 
        File "C:\Python26\lib\timeit.py", line 193, in timeit 
            timing = self.inner(it, self.timer) 
        File "", line 6, in inner 
    ZeroDivisionError: integer division or modulo by zero
    
А так будет выглядеть сообщение об ошибке, используя метод класса:

    except: 
        t.print_exc()
        
Результат:

    Traceback (most recent call last): 
      File "C:\Documents and Settings\User\tmp.py", line 43, in 
        t.timeit() 
      File "C:\Python26\lib\timeit.py", line 193, in timeit 
        timing = self.inner(it, self.timer) 
      File "", line 6, in inner 
        b=a/0 
    ZeroDivisionError: integer division or modulo by zero
    
Timer.timeit([number=1000000])

Эта команда выполнит выражение setup один раз, а затем возвратит время в секундах типа float, которое требуется что бы выполнить основное выражение number раз.

    Важно! По-умолчанию timeit() временно отключает сборщик мусора на время измерений. 
    реимущество этого поведения заключается в том, что независимые измерения становятся 
    более сопоставимыми. Недостатком же является то что сборщик мусора может быть важным 
    компонентом производительности исследуемой функции. В таком случае необходимо включить 
    сборщик мусора, используя выражение setup как показано в примере:
    
    timeit.Timer('for i in xrange(10): oct(i)', 'gc.enable()').timeit()
    

Timer.repeat([repeat=3[,number=1000000]])
Вызов timeit() c заданным repeat количеством раз, аргумент number передается в timeit().

    Очень заманчиво для вычисления среднего и стандартного отклонения от вектора результата и сообщать 
    о них. Однако, это не очень полезно. В типичном случае, наименьшее значение дает нижнюю границу 
    для того что бы понять, как быстро ваш компьютер может выполнить данный фрагмент кода, более 
    высокие значения в результате, как правило, вызваны не различиями в скорости Python, а 
    вмешательством других процессов в точность синхронизации. Так min() результата, наверное, 
    единственное значение, которое должно заинтересовать. После этого, вы должны смотреть на все 
    вектор и применять здравый смысл, а не статистику.
    
Начиная с версии 2.6 были добавлены 2 удобные функции.

    timeit.timeit(stmt[, setup[, timer[, number=1000000]]]])

Создает экземпляр класса Timer, передает в конструктор входные параметры, вызывает метод timeit(), возвращает результат в секундах типа float.

    timeit.repeat(stmt[, setup[, timer[, repeat=3[, number=1000000]]]])

Создает экземпляр класса Timer, передает в конструктор входные параметры, вызывает метод repeat(), возвращает список результатов.


### Пример

Следующий пример покажет, как можно реализовать проверку быстродействия методов класса.

    import time, timeit 
    
    class Test_class(object): 
        def some_slow_method(self, loop_count): 
            for i in xrange(loop_count): 
                time.sleep(1) 
    
        def some_quick_method(self, loop_count): 
            for i in xrange(loop_count): 
                time.sleep(0.1) 
    
    if __name__=='__main__': 
        # Для того что бы воспользоваться классом необходимого модуля, его необходимо импортировать в инициализирующем выражении setup 
        setup=""" 
    from __main__ import Test_class 
    test=Test_class() 
    """ 
        statements=['test.some_slow_method(5)', 
        'test.some_slow_method(3)', 
        'test.some_quick_method(5)', 
        'test.some_quick_method(3)'] 
        for item in statements: 
            print '%s execute in %s seconds'%(item, min(timeit.repeat(item, setup, timeit.default_timer, 3, 1)))
            
Результат выполнения:

    test.some_slow_method(5) execute in 4.99914006752 seconds 
    test.some_slow_method(3) execute in 2.99965849878 seconds 
    test.some_quick_method(5) execute in 0.502633834254 seconds 
    test.some_quick_method(3) execute in 0.301485550227 seconds
    
Пример сравнения быстродействия получения массива квадратов диапазона чисел:

    setup="data=range(1000)" 
    statements=[ 
            '[x*x for x in data]', 
    ''' 
    result=[] 
    for x in data: 
        result.append(x*x) 
    ''', 
            'map(lambda x: x*x, data)'] 
    for i in statements: 
        print timeit.repeat(i,setup,timeit.default_timer, 3,10000)
        
Результаты:

    [0.85908055846317666, 0.85963830564898203, 0.85809925998696102] 
    [1.7150783079655412, 1.6902710489738482, 1.698589834151278] 
    [2.1157915758631347, 2.116887527026563, 2.1211939035795169]
