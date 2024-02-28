### Yatube API Project

**For documentation in English, please refer to [README_EN.md](./README_EN.md).**


Yatube is a blogging platform. The project implements the following capabilities: registration, creation, editing or deleting posts, commenting on posts of another author and subscribing to him.

After the project is launched, documentation for the Yatube API will be available at http://127.0.0.1:8000/redoc/.

### Installation

Clone the repository and go to it on the command line:

```
git clone git@github.com:dodonova/api-blog-service-yatube.git
```

```
cd api_final_yatube
```

In the same folder create `.env` file and put there information about environment variables. 

Example in the file [.env.example](./.env.example)    

Create and activate a virtual environment:

```
python3 -m venv env
```

* If you have Linux/macOS

     ```
     source env/bin/activate
     ```

* If you have windows

     ```
     source env/scripts/activate
     ```

```
python3 -m pip install --upgrade pip
```

Install dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

Run migrations:

```
python3 manage.py migrate
```

Run the project:

```
python3 manage.py runserver
```

### Examples

Example of a POST request with a user token: adding a new post.

*POST .../api/v1/posts/*

```
{
     "text": "Post text.",
     "group": 1
}
```

Sample answer:

```
{
     "id": 14,
     "text": "Post text.",
     "author": "user",
     "image": null,
     "group": 1,
     "pub_date": "2021-06-01T08:47:11.084589Z"
}
```

An example of a POST request to add a new comment to a post with `id=14`.

*POST .../api/v1/posts/14/comments/*

```
{
     "text": "test test"
}
```

Sample answer:

```
{
     "id": 4,
     "author": "user",
     "post": 14,
     "text": "test test",
     "created": "2021-06-01T10:14:51.388932Z"
}
```

An example of a GET request to obtain information about a group.

GET *.../api/v1/groups/2/*

Sample answer:

`{
     "id": 2,
     "title": "Mathematics",
     "slug": "math",
     "description": "Mathematics related posts"
}`