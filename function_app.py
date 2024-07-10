import logging
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="0 0 0 * * 0", arg_name="myTimer", run_on_startup=True, use_monitor=False)
def timer_trigger_spotify_playlist(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    # Import your main logic here
    from main import run_main_logic
    run_main_logic()
