from plyer import notification
title = 'Just checking on you!'

message= 'Time to drink some water!'
notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=True)
