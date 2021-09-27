def timetable_routes(api, app, root="api"):
    from app.score_based_study_hour import timetable_routes as attach_timetable
  

    # Add routes
    attach_timetable(api, app)