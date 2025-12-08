
def check_brick_collisions(game):
    """Handle brick collision logic"""
    for brick in game.bricks:
        #ball and brick collision
        if game.ball.rect.colliderect(brick):
            #brick bottom
            if (
            game.ball.vector.y < 0 #moving upwards
            and (game.ball.x+game.ball.rect.width > brick.rect.x)
            and (game.ball.x < brick.rect.x+brick.rect.width) #x position
            and (game.ball.y <= brick.rect.y+brick.rect.height+game.settings.coll_tol)
            and (game.ball.y >= brick.rect.y+brick.rect.height-game.settings.coll_tol) #y position
            ):
                game.ball.vector.y = game.ball.vector.y * -1 #flip y vector
                game.bricks.remove(brick)
                break
            #brick top
            if (
            game.ball.vector.y > 0 #moving downwards
            and (game.ball.x+game.ball.rect.width > brick.rect.x)
            and (game.ball.x < brick.rect.x+brick.rect.width) #x position
            and (game.ball.y+game.ball.rect.height >= brick.rect.y-game.settings.coll_tol)
            and (game.ball.y+game.ball.rect.height <= brick.rect.y+game.settings.coll_tol) #y position
            ):
                game.ball.vector.y = game.ball.vector.y * -1 #flip y vector
                game.bricks.remove(brick)
                break
            #brick right
            if (
            game.ball.vector.x < 0 #moving left
            and (game.ball.x <= brick.rect.x+brick.rect.width+game.settings.coll_tol)
            and (game.ball.x >= brick.rect.x+brick.rect.width-game.settings.coll_tol) #x position
            and (game.ball.y < brick.rect.y+brick.rect.height)
            and (game.ball.y+game.ball.rect.height > brick.rect.y) #y position
            ):
                game.ball.vector.x = game.ball.vector.x * -1 #flip x vector
                game.bricks.remove(brick)
                break
            #brick left
            if (
            game.ball.vector.x > 0 #moving right
            and (game.ball.x+game.ball.rect.width >= brick.rect.x-game.settings.coll_tol)
            and (game.ball.x+game.ball.rect.width <= brick.rect.x+game.settings.coll_tol) #x position
            and (game.ball.y < brick.rect.y+brick.rect.height)
            and (game.ball.y+game.ball.rect.height > brick.rect.y) #y position
            ):
                game.ball.vector.x = game.ball.vector.x * -1 #flip x vector
                game.bricks.remove(brick)
                break

def check_bumper_collisions(game):
    """Handle bumper collision logic"""
    if game.ball.rect.colliderect(game.bumper):
        #top collison
        if (
        (game.ball.x+game.ball.rect.width > game.bumper.rect.x)
        and (game.ball.x < game.bumper.rect.x+game.bumper.rect.width) #x position
        and (game.ball.y+game.ball.rect.height >= game.bumper.rect.y-3)
        and (game.ball.y+game.ball.rect.height <= game.bumper.rect.y+3) #y position
        ):
            game.ball.vector.y = game.ball.vector.y * -1
        #left collision
        if (
        (game.ball.x+game.ball.rect.width >= game.bumper.rect.x-3)
        and (game.ball.x+game.ball.rect.width <= game.bumper.rect.x+3) #x position
        and (game.ball.y < game.bumper.rect.y+game.bumper.rect.height)
        and (game.ball.y+game.ball.rect.height > game.bumper.rect.y) #y position
        ):
            game.ball.vector.x = game.ball.vector.x * -1 #flip x vector
        #right collision
        if (
        (game.ball.x <= game.bumper.rect.x+game.bumper.rect.width+3)
        and (game.ball.x >= game.bumper.rect.x+game.bumper.rect.width-3) #x position
        and (game.ball.y < game.bumper.rect.y+game.bumper.rect.height)
        and (game.ball.y+game.ball.rect.height > game.bumper.rect.y) #y position
        ):
            game.ball.vector.x = game.ball.vector.x * -1 #flip x vector

def check_wall_collisions(game):
    """Handle wall collision logic"""
    if game.ball.rect.colliderect(game.settings.right_edge):
        game.ball.vector.x = game.ball.vector.x * -1
    if game.ball.rect.colliderect(game.settings.left_edge):
        game.ball.vector.x = game.ball.vector.x * -1
    if game.ball.rect.colliderect(game.settings.top_edge):
        game.ball.vector.y = game.ball.vector.y * -1
    if game.ball.rect.colliderect(game.settings.bottom_edge):
        game.ball.moving =  False
        game.ball.reset_pos()