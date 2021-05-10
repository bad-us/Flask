# from blog.app import app
#
# if __name__ == '__main__':
#     app.run(
#         host='127.0.0.1',
#         debug=True,
#         port=5000,
#     )

from blog.app import create_app

app = create_app()

app.run(debug=True)
