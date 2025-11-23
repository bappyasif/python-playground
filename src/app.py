from fastapi import FastAPI, HTTPException

from src.schemas import PostCreate, PostResponse

from typing import List, Dict

app = FastAPI()

posts = {
    1: {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    2: {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2
    },
    3: {
        "title": "title of post 3",
        "content": "content of post 3",
        "id": 3
    },
    4: {
        "title": "title of post 4",
        "content": "content of post 4",
        "id": 4
    },
    5: {
        "title": "title of post 5",
        "content": "content of post 5",
        "id": 5
    },
    6: {
        "title": "title of post 6",
        "content": "content of post 6",
        "id": 6
    }
}

# this is a much better typed version where return response is also typed for fastapi docs
@app.post("/create-a-post")
def create_a_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content, "id": len(posts) + 1}
    posts[max(posts.keys()) + 1] = new_post
    return new_post
    # return "wrong" # this will not work as the return type is PostResponse anything other than PostResponse will not work


@app.post("/create-post")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content, "id": len(posts) + 1}
    posts[max(posts.keys()) + 1] = new_post
    return new_post


# @app.post("/posts")
# def create_post(post: dict):
#     post_id = len(posts) + 1
#     post["id"] = post_id
#     posts[post_id] = post
#     return posts[post_id]


# request with query parameters
# @app.get("/query/posts?limit={limit}") # this will not work as {} are used to define patha parameters not query parameters
@app.get("/query/posts")
def get_posts_by_query(limit: int):
    return {"posts": list(posts.items())[:limit]}
# @app.get("/query/posts?limit={limit}")
# def get_post_by_query(limit: int):
#     return {"posts": posts[:limit]}

@app.get("/posts/${id}")
def get_post(id: int):
    if id not in posts:
        raise HTTPException(status_code=404, detail="Post is not found!")
        # return {"message": "Post is not found!"}
    
    return posts.get(id)
    # return {"post": posts[id]} # this is another way

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        # return {"posts": posts[:limit]}
        # print(posts[0:limit])
        # return posts[0:limit]
        # print(limit, list(posts.items())[:limit])
        # return {"msg": "trying"}
        return {"posts": list(posts.items())[:limit]}
    
    return {"posts": posts}

# this is a much better typed version where return response is also typed for fastapi docs
@app.get("/posts-v2")
def get_all_posts_v2(limit: int = None) -> Dict[str, List]:
    if limit:
        posts_list = list(posts.items())[:limit]
    else:
        posts_list = list(posts.items())
    
    return {"posts": posts_list}

# @app.get("/posts-v2")
# def get_all_posts_v2(limit: int = None) -> List[PostResponse]:
#     if limit:
#         posts_list = list(posts.items())[:limit]
#     else:
#         posts_list = posts.items()
    
#     return [{"id": post["id"], "title": post["title"], "content": post["content"]} for post in posts_list]
        # return {"posts": list(posts.items())[:limit]}
    # return {"posts": posts}
    # return {"posts": list(posts.items())}
    return list(posts.items())

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"}
