import 'dart:io';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:image_cropper/image_cropper.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());


class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CBC Diagnosis',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
        brightness: Brightness.dark,
      ),
      home: ImageCapture(),
    );
  }
}

// Widget to capture and crop the image
class ImageCapture extends StatefulWidget{

  createState() => _ImageCaptureState();
}


class _ImageCaptureState extends State<ImageCapture> {
  /// Active image file
  File _imageFile;

  /// Cropper plugin
  Future<void> _cropImage() async {
    File cropped = await ImageCropper.cropImage(
        sourcePath: _imageFile.path,
//        aspectRatioPresets: [
//          CropAspectRatioPreset.square,
//          CropAspectRatioPreset.ratio3x2,
//          CropAspectRatioPreset.original,
//          CropAspectRatioPreset.ratio4x3,
//          CropAspectRatioPreset.ratio16x9
//        ],
//        androidUiSettings: AndroidUiSettings(
//          toolbarColor: Colors.purple,
//          toolbarWidgetColor: Colors.white,
//          toolbarTitle: 'Crop It'
//        ),
//        iosUiSettings: IOSUiSettings(
//          minimumAspectRatio: 1.0,
//        )
    );

    setState(() {
      _imageFile = cropped ?? _imageFile;
    });
  }

  /// Select an image via gallery or camera
  Future<void> _pickImage(ImageSource source) async {
    File selected = await ImagePicker.pickImage(source: source);

    setState(() {
      _imageFile = selected;
    });
  }

  /// Remove image
  void _clear() {
    setState(() => _imageFile = null);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: BottomAppBar(
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            IconButton(
              icon: Icon(
                Icons.photo_camera,
                size: 30,
              ),
              onPressed: () => _pickImage(ImageSource.camera),
              color: Colors.blue,
            ),
            IconButton(
              icon: Icon(
                Icons.photo_library,
                size: 30,
              ),
              onPressed: () => _pickImage(ImageSource.gallery),
              color: Colors.pink,
            ),
          ],
        ),
      ),
      body: ListView(
        children: <Widget>[
          if (_imageFile != null) ...[
            Container(
                padding: EdgeInsets.all(32), child: Image.file(_imageFile)),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                FlatButton(
                  color: Colors.black,
                  child: Icon(Icons.crop),
                  onPressed: _cropImage,
                ),
                FlatButton(
                  color: Colors.black,
                  child: Icon(Icons.refresh),
                  onPressed: _clear,
                ),
              ],
            ),
            Padding(
              padding: const EdgeInsets.all(32),
              child: Uploader(
                file: _imageFile,
              ),
            )
          ]
        ],
      ),
    );
  }
}

/// Widget used to handle the management of
class Uploader extends StatefulWidget {
  final File file;

  Uploader({Key key, this.file}) : super(key: key);

  createState() => _UploaderState();
}

class _UploaderState extends State<Uploader> {
  final String imageUploadEndPoint = 'http://192.168.0.109:8080/imageUpload';
  String status = '';
  String errMessage = 'Error Uploading Image';
  String resultBody = '';

  _startUpload() {
    setState(() {
      status = 'Uploading Image...';
    });
    String base64Image = base64Encode(widget.file.readAsBytesSync());
    String fileName = '${DateTime.now()}.png';
    http.post(imageUploadEndPoint, body: {
      "image": base64Image,
      "name": fileName,
    }).then((res) {
      setState(() {
        if(res.statusCode == 200){
          status = res.body;
        }else{
          status = errMessage;
        }
      });
    }).catchError((err) {
      print(err);
    });

  }

  @override
  Widget build(BuildContext context) {
    if(status!=''){
      return Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
              Text('🎉🎉🎉',
                  style: TextStyle(
                      color: Colors.greenAccent,
                      height: 2,
                      fontSize: 30)),
              Text(status,
                  style: TextStyle(
                      color: Colors.greenAccent,
                      height: 2,
                      fontSize: 30)),
          ]);
    }else{
      return FlatButton.icon(
          color: Colors.blue,
          label: Text('Upload to Server'),
          icon: Icon(Icons.cloud_upload),
          onPressed: _startUpload);
    }


  }
}

