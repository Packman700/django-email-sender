from django_newsletter.models.email_message import (EmailMessageCron, EmailMessageMembershipTime)

EmailMessageCron.objects.create(database_title="Mail to confirmed (Mo, We, Fr)",
                                title="I'm test mail",
                                content="if you see me you have proof that everything work fine ;D <br>"
                                        "I'm promise that I don't sending this mail manually <br>"
                                        "<small> This message is send by schedule cron schedule feature </small>",
                                cron="59 23 * * 1,3,5",
                                send_to_confirmed=True,
                                send_to_not_confirmed=False)

EmailMessageCron.objects.create(database_title="Mail to confirmed (Tu, Th, Sa)",
                                title="Test mail from django-newsletter",
                                content="If you enter this message i want wish you a good day :> <br>"
                                        "<small> This message is send by schedule cron schedule feature </small>",
                                cron="59 23 * * 2,4,6",
                                send_to_confirmed=True,
                                send_to_not_confirmed=False)

EmailMessageCron.objects.create(database_title="Mail to confirmed (Su)",
                                title="Sunday test mail",
                                content="Dude I know that my newsletter is awesome "
                                        "but you should chill in Sunday ;P <br>"
                                        "I recommend watch some good film "
                                        "(did you see Forest Gump) or go walk with dog <br>"
                                        "<small> This message is send by schedule cron schedule feature </small>",
                                cron="59 23 * * 0",
                                send_to_confirmed=True,
                                send_to_not_confirmed=False)

EmailMessageMembershipTime.objects.create(database_title="Mail to confirmed after one day",
                                          title="I'm happy that you with me",
                                          content="Welcome in second day of testing my newsletter <br>"
                                                  "<small> This message is send by schedule mail "
                                                  "according to time from join feature </small>",
                                          days_from_join=1,
                                          send_to_confirmed=True,
                                          send_to_not_confirmed=False)

EmailMessageMembershipTime.objects.create(database_title="Mail to not confirmed after one day",
                                          title="Let's try newsletter",
                                          content="I see that you don't confirm your mail if you forget about this "
                                                  "please click link in last mail and click link to confirm membership <br>"
                                                  "<small> This message is send by schedule mail "
                                                  "according to time from join feature </small>",
                                          days_from_join=1,
                                          send_to_confirmed=False,
                                          send_to_not_confirmed=True)