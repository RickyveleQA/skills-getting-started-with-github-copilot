def test_signup_successful(client, reset_activities):
    """Test successful signup for an activity"""
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert email in response.json()["message"]


def test_signup_activity_not_found(client):
    """Test signup for non-existent activity"""
    # Arrange
    email = "test@mergington.edu"
    invalid_activity = "NonexistentClub"
    
    # Act
    response = client.post(
        f"/activities/{invalid_activity}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_signup_duplicate_rejection(client, reset_activities):
    """Test that duplicate signup is rejected"""
    # Arrange
    email = "michael@mergington.edu"  # Already in Chess Club
    activity = "Chess Club"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_signup_multiple_activities(client, reset_activities):
    """Test that a student can sign up for multiple activities"""
    # Arrange
    email = "learner@mergington.edu"
    activities_to_join = ["Chess Club", "Programming Class"]
    
    # Act
    responses = [
        client.post(f"/activities/{activity}/signup", params={"email": email})
        for activity in activities_to_join
    ]
    
    # Assert
    for response in responses:
        assert response.status_code == 200
