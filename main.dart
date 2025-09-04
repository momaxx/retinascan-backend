import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() => runApp(RetinaScanApp());

class RetinaScanApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'RetinaScan Pro',
      home: Scaffold(
        appBar: AppBar(title: Text('RetinaScan Pro')),
        body: WebView(
          initialUrl: 'https://retinascan-pro.vercel.app',
          javascriptMode: JavascriptMode.unrestricted,
        ),
      ),
    );
  }
}
